import sys

china_map={
    '华南':{
        '广东':{'广州':['阿里','老男孩'],'佛山':['阿里','老男孩'],'深圳':['阿里','老男孩'],'东莞':['阿里','老男孩']},
        '广西':{'南宁':['阿里','老男孩'],'柳州':['阿里','老男孩'],'桂林':['阿里','老男孩'],'北海':['阿里','老男孩']},
        '海南':{'三亚':['阿里','老男孩'],'海口':['阿里','老男孩'],'三沙':['阿里','老男孩'],'詹州':['阿里','老男孩']},
        '香港':{'屯门':['阿里','老男孩'],'湾仔':['阿里','老男孩'],'北角':['阿里','老男孩'],'西贡':['阿里','老男孩']},
        '澳门':{'花地玛堂区':['阿里','老男孩'],'圣安多尼堂':['阿里','老男孩'],'望德堂区':['阿里','老男孩'],'大堂区':['阿里','老男孩']},
    },
    '华东':{
        '江苏':{'南京':['阿里','老男孩'],'无锡':['阿里','老男孩'],'徐州':['阿里','老男孩'],'苏州':['阿里','老男孩'],'常州':['阿里','老男孩']},
        '浙江':{'杭州':['阿里','老男孩'],'温州':['阿里','老男孩'],'宁波':['阿里','老男孩'],'台州':['阿里','老男孩'],'舟山':['阿里','老男孩']},
        '安徽':{'合肥':['阿里','老男孩'],'芜湖':['阿里','老男孩'],'蚌埠':['阿里','老男孩'],'滁州':['阿里','老男孩'],'阜阳':['阿里','老男孩'],'宿州':['阿里','老男孩'],'六安':['阿里','老男孩'],'宣城':['阿里','老男孩']},
        '福建':{'福州':['阿里','老男孩'],'厦门':['阿里','老男孩'],'泉州':['阿里','老男孩'],'漳州':['阿里','老男孩'],'莆田':['阿里','老男孩'],'龙岩':['阿里','老男孩']},
        '江西':{'南昌':['阿里','老男孩'],'景德镇':['阿里','老男孩'],'萍乡':['阿里','老男孩'],'九江':['阿里','老男孩'],'赣州':['阿里','老男孩'],'宜春':['阿里','老男孩']},
        '山东':{'济南':['阿里','老男孩'],'泰安':['阿里','老男孩'],'德州':['阿里','老男孩'],'曲阜':['阿里','老男孩']},
        '上海':{'黄埔':['阿里','老男孩'],'徐汇':['阿里','老男孩'],'长宁':['阿里','老男孩'],'虹口':['阿里','老男孩']},
    },
    '华中':{
        '湖北':{'武汉':['阿里','老男孩'],'黄石':['阿里','老男孩'],'十堰':['阿里','老男孩'],'襄阳':['阿里','老男孩'],'宜昌':['阿里','老男孩'],'鄂州':['阿里','老男孩'],'荆州':['阿里','老男孩']},
        '湖南':{'长沙':['阿里','老男孩'],'株洲':['阿里','老男孩'],'邵阳':['阿里','老男孩'],'岳阳':['阿里','老男孩'],'郴州':['阿里','老男孩']},
        '河南':{'郑州':['阿里','老男孩'],'开封':['阿里','老男孩'],'洛阳':['阿里','老男孩'],'焦作':['阿里','老男孩'],'平顶山':['阿里','老男孩']},
    },
    '华北':{
        '北京':{'东城':['阿里','老男孩'],'西城':['阿里','老男孩'],'朝阳':['阿里','老男孩'],'海淀':['阿里','老男孩'],'石景山':['阿里','老男孩'],'大兴':['阿里','老男孩'],'丰台':['阿里','老男孩'],'昌平':['阿里','老男孩']},
        '山西':{'太原':['阿里','老男孩'],'吕梁':['阿里','老男孩'],'晋中':['阿里','老男孩'],'长治':['阿里','老男孩'],'大同':['阿里','老男孩'],'阳泉':['阿里','老男孩'],'晋城':['阿里','老男孩'],'朔州':['阿里','老男孩'],'忻州':['阿里','老男孩'],'临汾':['阿里','老男孩']},
        '河北':{'石家庄':['阿里','老男孩'],'邯郸':['阿里','老男孩'],'廊坊':['阿里','老男孩'],'保定':['阿里','老男孩'],'张家口':['阿里','老男孩'],'唐山':['阿里','老男孩'],'秦皇岛':['阿里','老男孩'],'沧州':['阿里','老男孩']},
        '天津':{'和平区':['阿里','老男孩'],'河东区':['阿里','老男孩'],'河北区':['阿里','老男孩'],'南开区':['阿里','老男孩'],'武清':['阿里','老男孩']},
        '内蒙':{'呼和浩特':['阿里','老男孩'],'鄂尔多斯':['阿里','老男孩'],'乌海':['阿里','老男孩'],'通辽':['阿里','老男孩'],'呼伦贝尔':['阿里','老男孩'],'乌兰浩特':['阿里','老男孩']},
    },
    '西南':{
        '四川':{'成都':['阿里','老男孩'],'自贡':['阿里','老男孩'],'攀枝花':['阿里','老男孩'],'乐山':['阿里','老男孩'],'遂宁':['阿里','老男孩']},
        '云南':{'昆明':['阿里','老男孩'],'曲靖':['阿里','老男孩'],'玉溪':['阿里','老男孩'],'丽江':['阿里','老男孩'],'曲靖':['阿里','老男孩']},
        '贵州':{'贵阳':['阿里','老男孩'],'六盘水':['阿里','老男孩'],'遵义':['阿里','老男孩'],'安顺':['阿里','老男孩'],'毕节':['阿里','老男孩'],'铜仁':['阿里','老男孩']},
        '重庆':{'万州':['阿里','老男孩'],'涪陵':['阿里','老男孩'],'渝中':['阿里','老男孩'],'大渡口':['阿里','老男孩']},
        '西藏':{'拉萨':['阿里','老男孩'],'那曲':['阿里','老男孩'],'山南':['阿里','老男孩'],'昌都':['阿里','老男孩'],'林芝':['阿里','老男孩'],'日喀则':['阿里','老男孩']},
    },
    '西北':{
        '宁夏':{'银川':['阿里','老男孩'],'石嘴山':['阿里','老男孩'],'吴忠市':['阿里','老男孩'],'固原市':['阿里','老男孩'],'中卫市':['阿里','老男孩']},
        '陕西':{'西安':['阿里','老男孩'],'铜川':['阿里','老男孩'],'宝鸡':['阿里','老男孩'],'咸阳':['阿里','老男孩'],'渭南':['阿里','老男孩'],'汉中':['阿里','老男孩'],'榆林':['阿里','老男孩']},
        '甘肃':{'兰州':['阿里','老男孩'],'天水':['阿里','老男孩'],'张掖':['阿里','老男孩'],'酒泉':['阿里','老男孩'],'嘉峪关':['阿里','老男孩'],'庆阳':['阿里','老男孩'],'陇南':['阿里','老男孩']},
        '新疆':{'乌鲁木齐':['阿里','老男孩'],'克拉玛依':['阿里','老男孩'],'哈密':['阿里','老男孩'],'库尔勒':['阿里','老男孩'],'昌吉':['阿里','老男孩'],'博尔塔拉':['阿里','老男孩']},
    },
    '东北':{
        '黑龙江':{'哈尔滨':['阿里','老男孩'],'齐齐哈尔':['阿里','老男孩'],'鸡西':['阿里','老男孩'],'牡丹江':['阿里','老男孩'],'大兴安岭地区':['阿里','老男孩'],'黑河':['阿里','老男孩']},
        '吉林':{'长春':['阿里','老男孩'],'延吉':['阿里','老男孩'],'四平':['阿里','老男孩'],'吉林':['阿里','老男孩'],'松原':['阿里','老男孩']},
        '辽宁':{'沈阳':['阿里','老男孩'],'葫芦岛':['阿里','老男孩'],'大连':['阿里','老男孩'],'鞍山':['阿里','老男孩'],'营口':['阿里','老男孩'],'辽阳':['阿里','老男孩'],'朝阳':['阿里','老男孩']},
    }
}
#三级菜单
#可依次选择进入各子菜单
#area_map=china_map[area_list[int(area_num)]]

area_list = []
for i in china_map:
    area_list.append(i)     #i为华北，华中，注意字典是无序的

break_flag = False         #标志位
while not break_flag:
    for i in area_list:
        print(area_list.index(i),i)
    area_num = input("请输入选择的地区序号(q:quit;b:back)：")
    if area_num.isdigit():        #如果是数字
        if int(area_num) >= len(area_list):    #如果数字超界
            print("输入数字不能超过最大序号")
        else:            #进入下一级列表

            area_map = china_map[area_list[int(area_num)]]    #包括各省
            #print(area_map)        #易于调试
            province_list = []    #空列表，用来装省份
            for i in area_map:    #将选定省加入空列表
                province_list.append(i)

            break_provin_flag = False
            while not break_provin_flag:
                for i in province_list:
                    print(province_list.index(i), i)
                province_num = input("请输入选择的省份序号(q:quit;b:back)：")
                if province_num.isdigit():  # 如果是数字
                    if int(province_num) >= len(province_list):  # 如果数字超界
                        print("输入数字不能超过最大序号")
                    else:      #进入下一级列表

                        city_map = area_map[province_list[int(province_num)]]    #包括各市
                        #print(city_map)       #易于调试
                        city_list = []         #将各市放入空列表
                        for i in city_map:
                            city_list.append(i)
                        #print(city_list)      #易于调试
                        city_break_flag = False
                        while not city_break_flag:
                            for i in city_list:            #打印各市及序号
                                print(city_list.index(i), i)
                            city_num = input("请输入选定市的序号(q:quit;b:back)：")
                            if city_num.isdigit():      #是数字
                                if int(city_num) >= len(city_list):      #越界
                                    print("输入数字不能超过最大序号")
                                else:
                                    # 根据选定城市的序号，找到相应城市，再通过选定城市找到城市下的地区
                                    fina_map = city_map[city_list[int(city_num)]]
                                    #print(fina_map)     #易于调试
                                    fina_list = []
                                    for i in fina_map:
                                        fina_list.append(i)
                                    for i in fina_list:
                                        print(fina_list.index(i), i)
                                    print("END".center(50,'-'))

                            else:       #不是数字
                                if city_num == 'q':
                                    sys.exit()
                                elif city_num == 'b':
                                    city_break_flag = True
                                else:
                                    print("请输入数字")

                else:
                    if province_num == 'q':
                        sys.exit()
                    elif province_num == 'b':
                        break_provin_flag = True
                    else:
                        print("请输入数字")

    else:
        if area_num == 'q':      #返回
            break_flag = True
        elif area_num == 'b':
            print("已经是主界面，不能返回了SB")
        else:
            print("请输入数字")
