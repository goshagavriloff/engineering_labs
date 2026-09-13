from functools import wraps

class FeatureDecorator:
    @staticmethod
    def syncData(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            html, attr = self.__class__.html, self.__class__.attr
            factory = getattr(self, attr)
            
            result = func(self,*args, **kwargs)
            html.save(factory.df)

            return result
        return wrapper

    @staticmethod
    def getDoc(cls):
        parent_class = cls.__bases__[0] if cls.__bases__ else None
        
        for method_name, method in vars(cls).items():
            if callable(method) and not method_name.startswith("__"):
                
                parent_method = getattr(parent_class, method_name, None) if parent_class else None
                parent_doc = parent_method.__doc__ if parent_method else None
                
                if parent_doc:
                    @wraps(method)
                    def wrapper(self, *args, _func=method, _pdoc=parent_doc, **kwargs):
                        self._parent_doc = _pdoc
                        return _func(self, *args, **kwargs)

                    wrapper.__doc__ = parent_doc
                    setattr(cls, method_name, wrapper)
                    
        return cls
