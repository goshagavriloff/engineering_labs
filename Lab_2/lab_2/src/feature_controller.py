from lab_1 import WorkerController
from .html_controller import HtmlController
from .feature_decorator import FeatureDecorator

@FeatureDecorator.getDoc
class FeatureController(WorkerController):
    html=HtmlController()
    attr="_WorkerController__factory"

    def __init__(self):
        super().__init__()
        setattr(self, self.attr, self.html.load())


    @FeatureDecorator.syncData
    def create(self):
        return super().create()

    @FeatureDecorator.syncData
    def update(self):
        return super().update()


    @FeatureDecorator.syncData
    def delete(self):
        return super().delete()


    @FeatureDecorator.syncData
    def exit(self):
        return super().exit()

