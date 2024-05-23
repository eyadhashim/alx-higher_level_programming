#include <Python.h>
#include <stdio.h>
/**
 * print_python_float - gives data
 * @p: PyObject
 */
void print_python_float(PyObject *p)
{
	double result = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	result = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(result, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
/**
 * print_python_bytes - gives data
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
