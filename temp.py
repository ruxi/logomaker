from cStringIO import StringIO
import os, sys

def Sandbox(code):
    '''Given code as a string, execute it in a sandboxed python environment

    return the output, stderr, and any exception code
    '''
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()

    ns_globals = {}
    ns_locals = {}
    out, err, exc = None, None, None

    try:
        exec(code, ns_globals, ns_locals)
    except:
        import traceback
        exc = traceback.format_exc()

    out = redirected_output.getvalue()
    err = redirected_error.getvalue()

    # reset outputs to the original values
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    return out, err, exc


if __name__ == '__main__':
    content = sys.stdin.read()
    out, err, exc =  Sandbox(content)