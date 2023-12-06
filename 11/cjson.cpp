#include <Python.h>
#include <structmember.h>

static PyObject *cjson_loads(PyObject *self, PyObject *args);
static PyObject *cjson_dumps(PyObject *self, PyObject *args);

static PyMethodDef cjson_methods[] = {
        {"loads", cjson_loads, METH_VARARGS, "Load JSON string to Python dict."},
        {"dumps", cjson_dumps, METH_VARARGS, "Dump Python dict to JSON string."},
        {NULL, NULL, 0, NULL} /* Sentinel */
};

static struct PyModuleDef cjsonmodule = {
        PyModuleDef_HEAD_INIT,
        "cjson",
        NULL,
        -1,
        cjson_methods
};

PyMODINIT_FUNC PyInit_cjson(void) {
    return PyModule_Create(&cjsonmodule);
}


static PyObject *cjson_loads(PyObject *self, PyObject *args) {
    const char *json_str;

    if (!PyArg_ParseTuple(args, "s", &json_str)) {
        return NULL;
    }

    struct json_object *json_obj = json_tokener_parse(json_str);
    if (!json_obj) {
        PyErr_SetString(PyExc_ValueError, "Invalid JSON format");
        return NULL;
    }

    PyObject *result = PyDict_New();
    enum json_type type;
    json_object_object_foreach(json_obj, key, value) {
        // Convert json-c object to Python objects
        PyObject *py_key = Py_BuildValue("s", key);
        PyObject *py_value;

        switch (type = json_object_get_type(value)) {
            case json_type_int:
                py_value = Py_BuildValue("i", json_object_get_int(value));
                break;
            case json_type_string:
                py_value = Py_BuildValue("s", json_object_get_string(value));
                break;
            // Handle other types as needed
            default:
                PyErr_Format(PyExc_TypeError, "Unsupported JSON type: %d", type);
                Py_DECREF(result);
                return NULL;
        }

        PyDict_SetItem(result, py_key, py_value);
        Py_DECREF(py_key);
        Py_DECREF(py_value);
    }

    json_object_put(json_obj);
    return result;
}

static PyObject *cjson_dumps(PyObject *self, PyObject *args) {
    PyObject *py_dict;

    if (!PyArg_ParseTuple(args, "O", &py_dict)) {
        return NULL;
    }

    struct json_object *json_obj = json_object_new_object();

    PyObject *key, *value;
    Py_ssize_t pos = 0;

    while (PyDict_Next(py_dict, &pos, &key, &value)) {
        const char *c_key = PyUnicode_AsUTF8(key);
        enum json_type type = PyLong_Check(value) ? json_type_int : json_type_string;

        switch (type) {
            case json_type_int:
                json_object_object_add(json_obj, c_key, json_object_new_int(PyLong_AsLong(value)));
                break;
            case json_type_string:
                json_object_object_add(json_obj, c_key, json_object_new_string(PyUnicode_AsUTF8(value)));
                break;
            default:
                PyErr_Format(PyExc_TypeError, "Unsupported Python type: %d", type);
                json_object_put(json_obj);
                return NULL;
        }
    }

    const char *json_str = json_object_to_json_string(json_obj);
    PyObject *result = Py_BuildValue("s", json_str);

    json_object_put(json_obj);
    return result;
}
