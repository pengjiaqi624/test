import numpy as np

# 设置参数
ncols = 100
nrows = 100
xllcorner = 0.0
yllcorner = 0.0
cellsize = 10.0
nodata = -9999

# 生成地形数据：中心低(10m)，四周逐渐升高(15m)
x = np.linspace(-1, 1, ncols)
y = np.linspace(-1, 1, nrows)
X, Y = np.meshgrid(x, y)
# 简单的抛物面地形：Z = 10 + 5 * (X^2 + Y^2)
Z = 10 + 5 * (X**2 + Y**2)

# 写入文件
with open("dem.asc", "w") as f:
    f.write(f"ncols         {ncols}\n")
    f.write(f"nrows         {nrows}\n")
    f.write(f"xllcorner     {xllcorner}\n")
    f.write(f"yllcorner     {yllcorner}\n")
    f.write(f"cellsize      {cellsize}\n")
    f.write(f"NODATA_value  {nodata}\n")
    
    # 写入矩阵数据
    for row in Z:
        f.write(" ".join(map(lambda v: f"{v:.2f}", row)) + "\n")

print("成功生成 100x100 的 dem.asc 文件！")