import taichi as ti
ti.init()
S = ti.root.dynamic(ti.i, 1024, chunk_size=32)
x = ti.field(int)
S.place(x)
@ti.kernel
def add_data():
    for i in range(1000):
        x.append(i)
        print(x.length())

add_data()