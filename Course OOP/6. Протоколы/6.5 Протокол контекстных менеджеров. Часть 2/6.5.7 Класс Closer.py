class Closer:
    def __init__(self, obj):
        self._obj = obj

    def __enter__(self):
        return self._obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self._obj, 'close'):
            self._obj.close()
        else:
            print('Незакрываемый объект')
