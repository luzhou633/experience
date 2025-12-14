# 头歌实践作业四
"""
创建宠物寄养记录数据库，用字典对象保存寄养的宠物信息，
包括宠物编号、宠物名称、品种名称、寄养天数、主人称呼、主人嘱咐等。
要求支持下面的查询：
def query_pets(pets):
    cats = [pet for pet in pets if "猫" in pet["品种名称"]]
    print(f"猫的数量: {len(cats)}只")
    long_stay = [pet for pet in pets if pet["寄养天数"] > 15]
    print("\n寄养天数大于15的宠物:")
    for pet in long_stay:
        print(f"{pet['宠物名称']} ({pet['品种名称']}) - {pet['寄养天数']}天")
    bad_temper = [pet for pet in pets if "脾气不好" in pet["主人备注"] or "脾气暴躁" in pet["主人备注"]]
    print("\n主人备注中出现脾气问题的宠物:")
    for pet in bad_temper:
        print(f"{pet['宠物名称']} ({pet['品种名称']}) - 备注: {pet['主人备注']}")
    print("\n宠物寄养记录查询结束。")
"""
"""
参考课堂介绍的推荐系统案例，尝试把程序改成歌曲推荐程序：
有一组客户及其点歌的数据，为打算点歌的客户推荐歌曲
"""
def recommend_songs(customers, favorite_songs):
    # 统计每首歌的出现次数
    song_counts = {}
    for customer, songs in customers.items():
        for song in songs:
            if song in song_counts:
                song_counts[song] += 1
            else:
                song_counts[song] = 1

    # 找出与用户喜欢的歌最接近的客户
    recommended_songs = set()
    for song in favorite_songs:
        for customer, songs in customers.items():
            if song in songs:
                recommended_songs.update(songs)

    # 去掉用户已经喜欢的歌
    recommended_songs.difference_update(favorite_songs)

    print("与您最爱接近的客户还喜欢这些歌曲:")
    print(", ".join(recommended_songs))

# 示例客户数据
customers = {
    "客户1": {"断桥残雪", "领悟", "暗香", "隐形的翅膀", "再见", "白桦林", "流年", "一眼万年", "那些花儿", "雨一直下", "小城大事", "一剪梅"},
    "客户2": {"暗香", "水手", "朋友", "流年", "再回首", "老鼠爱大米", "曾经的你", "一剪梅", "你的样子"},
    "客户3": {"再回首", "黄昏"},
    "客户4": {"梦醒时分", "隐形的翅膀", "朋友", "棉花糖", "难念的经", "小城大事", "一剪梅"},
    "客户5": {"领悟", "父亲", "流年", "飘雪", "雨一直下", "童年", "遇见", "黄昏"},
    "客户6": {"隐形的翅膀", "父亲", "大海", "一眼万年", "那些花儿", "飘雪", "问桌的你", "棉花糖", "曾经的你", "一剪梅", "慢慢"},
    "客户7": {"遇见"},
    "客户8": {"父亲", "飘雪", "黄昏", "曲终人散", "老鼠爱大米", "一剪梅"},
    "客户9": {"领悟", "大海", "白桦林", "一剪梅", "问桌的你", "棉花糖", "难念的经", "曲终人散", "再回首", "黄昏", "你的样子"},
    "客户10": {"再见", "水手", "朋友", "流年", "飘雪", "问桌的你", "雨一直下", "我是女生", "曲终人散", "再回首", "一剪梅", "你的样子"}
}

# 用户输入喜欢的歌曲
favorite_songs = input("输入几首你喜欢的歌曲名称（用空格隔开）: ").split()

# 调用推荐函数
recommend_songs(customers, favorite_songs)