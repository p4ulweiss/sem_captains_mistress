# Observer Pattern

## Problem: 

In software applications, there are often scenarios where the state of an object changes, and other parts of the application need to be notified about it. For example, when the data in a data model changes, the associated views need to be updated. The problem is to find a clean way to manage the dependencies between these objects.

## Solution: 

The Observer Pattern  provides a solution to this problem by defining a dependency between objects, so that changes to one object can automatically be propagated to all dependent objects. It consists of two main components: the "Subject" and the "Observers". The "Subject" maintains a list of "Observers" and provides methods to add and remove "Observers". When the state of the "Subject" changes, it automatically notifies all its "Observers" so they can react to the change. Since the observer is in the list of the subject, the method e.g. update() in the observer is called.

Application: The Observer Pattern is commonly used in graphical user interface (GUI) frameworks, where changes to the model are reflected in the view. For instance, in a web browser, changes in the underlying HTML structure are automatically reflected in the rendered webpage, thanks to the Observer Pattern.

Short example code:

```python
class Subject:
    """Represents what is being observed"""
 
    def __init__(self):
        """create an empty observer list"""
        self._observers = []
 
    def notify(self, modifier = None):
        """Alert the observers"""
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)
                
     def attach(self, observer):
        """If the observer is not in the list,
        append it into the list"""
        if observer not in self._observers:
            self._observers.append(observer)
 
     def detach(self, observer):
     """Remove the observer from the observer list"""
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
          
class Data(Subject):
    """monitor the object"""
 
    def __init__(self, name =''):
        Subject.__init__(self)
        self.name = name
        self._data = 0
 
    @property
    def data(self):
        return self._data
 
    @data.setter
    def data(self, value):
        self._data = value
        self.notify()
        
class Viewer:
    """Logs if a subject gets data"""
    def update(self, subject):
        print(f'Viewer: Subject {subject.name} has data - {subject.data}')
        
if __name__ == "__main__":
    """provide the data"""
    obj1 = Data('Data 1')
    view1 = Viewer()
    
    obj1.attach(view1)
    #Since observers is a list, it is possible to attach multiple observers
    
    obj1.data = 1
    #output from viewer
    
```