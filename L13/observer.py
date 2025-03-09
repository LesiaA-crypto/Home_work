Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Sub:
    def react(self, creator):
        print("Sub реагирует лайком на новое видео От:")
        print(creator)

        
class Creator:
    subs = []
    def __init__(self, name):
        self.subs = []
        self.name = name
    def __str__(self):
        return f"{self.name}"
    def follow(self, sub):
        self.subs.append(sub)
...         print("подписчик успешно подписался.")
...     def notify_all(self):
...         for sub in self.subs:
...             sub.react(self)
...     def create_event(self):
...         print("произошло новое видео.")
...         self.notify_all()
... 
...         
>>> chan_owner = Creator("Channel")
>>> chan_owner.subs
[]
>>> chan_owner.name
'Channel'
>>> sub1 = Sub()
>>> sub2 = Sub()
>>> sub3 = Sub()
>>> chan_owner.follow(sub1)
подписчик успешно подписался.
>>> chan_owner.follow(sub2)
подписчик успешно подписался.
>>> chan_owner.subs
[<__main__.Sub object at 0x000002C61532DF10>, <__main__.Sub object at 0x000002C612C693D0>]
>>> chan_owner.create.event()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    chan_owner.create.event()
AttributeError: 'Creator' object has no attribute 'create'
>>> chan_owner.Creator.event()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    chan_owner.Creator.event()
AttributeError: 'Creator' object has no attribute 'Creator'
