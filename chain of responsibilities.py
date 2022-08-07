"""  Chain of responsibilties pattern"""

from abc import abstractclassmethod


class Handler:
    @abstractclassmethod
    def set_next(self, handler):
        pass

    @abstractclassmethod
    def handle(self, request):
        pass

class AbstractHandler(Handler):
    """  The _next_handler is object of handle class"""
    _next_handler=None 
    
    @classmethod
    def set_next(self,handler):
        self._next_handler=handler
        return handler

    @abstractclassmethod
    def handle(self,request):
        if self._next_handler:
            self._next_handler.handle(request)

class BasicAuthenticator(AbstractHandler):

    @classmethod
    def handle(self,request):
        if request=="Basic":
            print(" The request is authenticated for basic")
        else:
            super().handle(request)

class AdvancedAuthenticator(AbstractHandler):

    @classmethod
    def handle(self,request):
        if request=="Advanced":
            print(" The request is authenticated for advanced")
        else:
            super().handle(request)

class supremeAuthenticator(AbstractHandler):

    @classmethod
    def handle(self,request):
        if request=="Supreme":
            print(" The request is authenticated for supreme")
          
        else:
            super().handle(request)


supreme=supremeAuthenticator()
basic=BasicAuthenticator()
advanced=AdvancedAuthenticator()
supreme.set_next(advanced).set_next(basic)
supreme.handle("Supreme")
supreme.handle("Basic")
