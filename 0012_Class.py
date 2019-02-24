class MyClass:
    def function(self):
        return "Hello,Pythonのオブジェクト指向"

class MyClass1:                                  #CLASS宣言
    def function(self):                         #メソッド宣言
        sys.stdout.write('MyClass1')#インスタンス宣言
        return ""

class MyClass2:                                  #CLASS宣言
    def function(self):                         #メソッド宣言
        sys.stdout.write('MyClass2')#インスタンス宣言
        return ""





c = MyClass()
print(c.function())#メソッド実行


c1 = MyClass1()#オブジェクト作成
c2 = MyClass2()#オブジェクト作成

print(c1.function())#メソッド実行
print(c2.function())#メソッド実行