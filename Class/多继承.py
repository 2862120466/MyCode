class Ma:
    def run(self):
        print("马跑得快")

    def far(self):
        print("马走不远")


class Lv:
    def run(self):
        print("驴跑的慢")


class Luozi(Ma, Lv):
    pass


luozi = Luozi()
luozi.far()
luozi.run()
print(Luozi.mro()) # 显示调用父类方法的顺序