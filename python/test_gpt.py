import itertools

# 定义饮料和小吃的列表
drinks = ['咖啡', '茶', '果汁']
snacks = ['饼干', '蛋糕', '水果']

# 使用笛卡尔积生成所有可能的组合
combinations = list(itertools.product(drinks, snacks))

# 打印组合
for combo in combinations:
    print(f"饮料: {combo[0]}, 小吃: {combo[1]}")
