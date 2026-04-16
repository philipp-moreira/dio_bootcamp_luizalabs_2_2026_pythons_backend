class My_Class:
    this_is_my_class_attribute = 'I am static, that is, I will be unique regardless of which instance (object) calls me (consumes me).'

    def __init__(self):
        self.this_is_my_object_attribute = (
            'I am not static, that is, I will be unique per instance (object).'
        )


obj0 = My_Class()
obj1 = My_Class()
obj2 = My_Class()

print('obj0.this_is_my_class_attribute ==> ', obj0.this_is_my_class_attribute)
print('obj1.this_is_my_class_attribute ==> ', obj1.this_is_my_class_attribute)
print('obj2.this_is_my_class_attribute ==> ', obj2.this_is_my_class_attribute)

print('-' * 20)

print('obj0.this_is_my_object_attribute ==> ', obj0.this_is_my_object_attribute)
print('obj1.this_is_my_object_attribute ==> ', obj1.this_is_my_object_attribute)
print('obj2.this_is_my_object_attribute ==> ', obj2.this_is_my_object_attribute)

print('-' * 20)

obj0.this_is_my_class_attribute = (
    "I don't have encapsulation, that is, if a consumer changes me, I will be changed."
)
print('obj0.this_is_my_class_attribute ==> ', obj0.this_is_my_class_attribute)

print('-' * 20)

obj1.this_is_my_object_attribute = 'I am unique, I can be changed, without affecting other objects that have the same class as me.'
print('obj0.this_is_my_object_attribute ==> ', obj0.this_is_my_object_attribute)
print('obj1.this_is_my_object_attribute ==> ', obj1.this_is_my_object_attribute)
print('obj2.this_is_my_object_attribute ==> ', obj2.this_is_my_object_attribute)
