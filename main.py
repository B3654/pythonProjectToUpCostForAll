# имя файла - имя поставщика и дата обновления
import os
import pathlib
import datetime
import socket
import io
import json


def check_computer_name():
    if socket.gethostname() == "DESKTOP-KNALPLF" or socket.gethostname() == "DESKTOP-FOLH85B" or socket.gethostname() == "DESKTOP-B5UPGHV" \
            or socket.gethostname() == "DESKTOP-PNM1B2P":
        pass
    else:
        exit()

def deleate_old_files():
    try:
        for f in os.listdir("актуальные_цены/"):
            os.remove(os.path.join("актуальные_цены/", f))
    except:
        print("Ошибка при удалении старых файлов")

def is_number(my_str):
    try:
        float(my_str)
        return True
    except ValueError:
        return False


def config_variable_price():
    with open('config_files/конфигурационный_файл_как_поднимать_цену.txt', encoding="utf-8") as config:
        dict_start_price = json.loads(str(config.readlines(1)).replace('[', '').replace(']', '').replace("\\n", '').replace("'", ""))
        dict_upper_price = json.loads(str(config.readlines(2)).replace('[', '').replace(']', '').replace("\\n", '').replace("'", ""))
        dict_price = dict_start_price | dict_upper_price
        return dict_price


def to_one_type_of_text_file(txt_file):
    with io.open(txt_file, 'r', encoding="utf-8", errors='ignore') as f:
        lines = f.readlines()

        lines = [line.lower().replace('1tb', '1 tb') for line in lines]
        lines = [line.lower().replace('128gb', '128 gb') for line in lines]
        lines = [line.lower().replace('64gb', '64 gb') for line in lines]
        lines = [line.lower().replace('256gb', '256 gb') for line in lines]
        lines = [line.lower().replace('512gb', '512 gb') for line in lines]
        lines = [line.lower().replace('airpods2', 'AirPods 2') for line in lines]
        lines = [line.lower().replace('airpods3', 'AirPods 3') for line in lines]
        lines = [line.lower().replace('air pods', 'airpods') for line in lines]
        lines = [line.lower().replace('pro2', 'Pro 2') for line in lines]
        lines = [line.lower().replace('pro1', 'Pro 2') for line in lines]
        lines = [line.lower().replace('pro11', 'Pro 11') for line in lines]
        lines = [line.lower().replace('pro12.9', 'Pro 12.9') for line in lines]
        lines = [line.lower().replace('–', '-') for line in lines]
        lines = [line.lower().replace('.', '') for line in lines]
        lines = [line.lower().replace(',', '') for line in lines]
        lines = [line.lower().lstrip() for line in lines]

    # finally, write lines in the file
    with io.open(txt_file, 'w', encoding="utf-8", errors='ignore') as f:
        f.writelines(lines)


def start_to_one_type_of_text_file():
    for txt_file in pathlib.Path('поставщики/').glob('*.txt'):
        to_one_type_of_text_file(txt_file)


def cost_upper():
    config_variable_price()

    for txt_file in pathlib.Path('поставщики/').glob('*.txt'):
        new_file_name = str(txt_file.name).replace('.txt', ' ') + str(datetime.datetime.today().strftime("%d.%m")) + str('.txt')

        with io.open(txt_file, 'r', encoding="utf-8", errors='ignore') as f, io.open(f'актуальные_цены/{new_file_name}', 'w+', encoding='utf-8', errors='ignore') as dest:
            for line in f.readlines():
                if line.__contains__('-'):
                    a = line.split('-')[-1:]
                    astra = ' '.join(a)
                    if astra.__contains__(','):
                        astra1 = str.replace(astra, ',', '')
                        line = line.replace(str(astra), str(astra1)) + '\n'
                    elif astra.__contains__('.'):
                        astra1 = str.replace(astra, '.', '')
                        line = line.replace(str(astra), str(astra1)) + '\n'

                    while True:
                        if is_number(astra):
                            break

                        elif astra == "":
                            break

                        else:
                            astra = astra[:-1]

                    q = config_variable_price()["q"]
                    w = config_variable_price()["w"]
                    e = config_variable_price()["e"]
                    r = config_variable_price()["r"]
                    t = config_variable_price()["t"]
                    y = config_variable_price()["y"]
                    u = config_variable_price()["u"]
                    i = config_variable_price()["i"]
                    o = config_variable_price()["o"]
                    p = config_variable_price()["p"]
                    a = config_variable_price()["a"]
                    s = config_variable_price()["s"]
                    d = config_variable_price()["d"]
                    f = config_variable_price()["f"]
                    g = config_variable_price()["g"]
                    q1 = config_variable_price()["q1"]
                    w1 = config_variable_price()["w1"]
                    e1 = config_variable_price()["e1"]
                    r1 = config_variable_price()["r1"]
                    t1 = config_variable_price()["t1"]
                    y1 = config_variable_price()["y1"]
                    u1 = config_variable_price()["u1"]
                    i1 = config_variable_price()["i1"]
                    o1 = config_variable_price()["o1"]
                    p1 = config_variable_price()["p1"]
                    a1 = config_variable_price()["a1"]
                    s1 = config_variable_price()["s1"]
                    d1 = config_variable_price()["d1"]
                    f1 = config_variable_price()["f1"]
                    g1 = config_variable_price()["g1"]
                    h1 = config_variable_price()["h1"]

                    if astra == "":
                        dest.write(line)
                        continue

                    if int(astra) < q:
                        finish_summa = int(astra) + q1

                    elif q <= int(astra) < w:
                        finish_summa = int(astra) + w1

                    elif w <= float(astra) < e:
                        finish_summa = int(astra) + e1

                    elif e <= float(astra) < r:
                        finish_summa = int(astra) + r1

                    elif r <= float(astra) < t:
                        finish_summa = int(astra) + t1

                    elif t <= int(astra) < y:
                        finish_summa = int(astra) + y1

                    elif y <= float(astra) < u:
                        finish_summa = int(astra) + u1

                    elif u <= float(astra) < i:
                        finish_summa = int(astra) + i1

                    elif i <= float(astra) < o:
                        finish_summa = int(astra) + o1

                    elif o <= float(astra) < p:
                        finish_summa = int(astra) + p1

                    elif p <= int(astra) < a:
                        finish_summa = int(astra) + a1

                    elif a <= float(astra) < s:
                        finish_summa = int(astra) + s1

                    elif s <= float(astra) < d:
                        finish_summa = int(astra) + d1

                    elif d <= float(astra) < f:
                        finish_summa = int(astra) + f1

                    elif f <= float(astra)< g:
                        finish_summa = int(astra) + g1

                    elif float(astra) >= g:
                        finish_summa = int(astra) + h1

                    else:
                        dest.write(line)
                        continue

                    line = line.replace(str(astra), str(finish_summa)) + '\n'
                    dest.write(line)
                else:
                    pass


def all_in_one_file():
    try:
        with io.open('config_files/all_in_one.txt', 'w', encoding='utf-8', errors='ignore') as file_on_in_one:
            for txt_file in pathlib.Path('актуальные_цены').glob('*.txt'):
                with io.open(txt_file, encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        if line.isspace():
                            pass
                        else:
                            try:
                                file_on_in_one.write(
                                    line.replace('\n', '') + ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>: " + f.name.replace(
                                        'актуальные_цены\\', '') + '\n')
                            except:
                                print("не получилось удалить пробелы при привидении к одинаковому формату")
    except ValueError:
        print("Ошибка при создании объединенного файла всех поставщиков")


def write_to_head(txt_file):
    try:
        with open('config_files/конфигурационный_файл_как_поднимать_цену.txt', encoding="utf-8") as config:
            line = config.readlines()
            head = line[3:10]

        with io.open(txt_file, 'r', encoding="utf-8", errors='ignore') as f:
            lines = f.readlines()

        # finally, write lines in the file
        with io.open(txt_file, 'w', encoding="utf-8", errors='ignore') as f:
            f.writelines(str(datetime.datetime.today().strftime("%d.%m.%Y \n")))
            f.writelines(head)
            f.writelines(lines)

    except:
        print("Возникла ошибка при создании шапки")


def sort():
    try:
        with io.open('config_files/all_in_one.txt', 'r', encoding='utf-8', errors='ignore') as file_on_in_one, io.open(
                'отсортированный_файл/отсортированный_файл.txt', 'w', encoding='utf-8', errors='ignore') as sorted_file:
            data = file_on_in_one.readlines()
            data.sort()
            for i in range(len(data)):
                if data[i].isspace():
                    pass
                else:
                    sorted_file.write(data[i])

    except:
        print("Возникла ошибка при сортировке")


def sort_to_files():
    try:
        with io.open('отсортированный_файл_без_поставщиков/Айфоны.txt','w+', encoding='utf-8', errors='ignore') as file_iphone,\
                io.open('отсортированный_файл_без_поставщиков/ipad.txt', 'w+', encoding='utf-8', errors='ignore') as file_ipad,\
                io.open('отсортированный_файл_без_поставщиков/airpods.txt', 'w+', encoding='utf-8', errors='ignore') as file_airpods,\
                io.open('отсортированный_файл_без_поставщиков/watch.txt', 'w+', encoding='utf-8', errors='ignore') as file_watch,\
                io.open('отсортированный_файл_без_поставщиков/AirTag.txt', 'w+', encoding='utf-8', errors='ignore') as file_AirTag,\
                io.open('отсортированный_файл_без_поставщиков/Pencil.txt', 'w+', encoding='utf-8', errors='ignore') as file_Pencil,\
                io.open('отсортированный_файл_без_поставщиков/MacbookImac.txt', 'w+', encoding='utf-8', errors='ignore') as file_Macbook,\
                io.open('отсортированный_файл_без_поставщиков/Dyson.txt', 'w+', encoding='utf-8', errors='ignore') as file_Dyson,\
                io.open('отсортированный_файл_без_поставщиков/TV.txt', 'w+', encoding='utf-8', errors='ignore') as file_TV,\
                io.open('отсортированный_файл_без_поставщиков/android.txt', 'w+', encoding='utf-8', errors='ignore') as android,\
                io.open('отсортированный_файл_без_поставщиков/xbox_ps4.txt', 'w+', encoding='utf-8', errors='ignore') as xbox_ps4,\
                io.open('отсортированный_файл_без_поставщиков/аксессуары.txt', 'w+', encoding='utf-8', errors='ignore') as accessories,\
                io.open('отсортированный_файл_без_поставщиков/колонки.txt', 'w+', encoding='utf-8', errors='ignore') as column,\
                io.open('отсортированный_файл_без_поставщиков/gopro.txt', 'w+', encoding='utf-8', errors='ignore') as gopro,\
                io.open('отсортированный_файл_без_поставщиков/квадрокоптеры.txt', 'w+', encoding='utf-8', errors='ignore') as quadrocopter,\
                io.open('отсортированный_файл_без_поставщиков/Планшеты_андроид.txt', 'w+', encoding='utf-8', errors='ignore') as tablet,\
                io.open('отсортированный_файл_без_поставщиков/отсортированный_файл_без_поставщиков.txt', 'r', encoding='utf-8', errors='ignore') as sorted_file:

            file_iphone.write("📱🍏 iphone 🍏📱\n")
            file_ipad.write("🔥🍏 Ipad ⌨️🍏🔥\n")
            tablet.write("🔥 Планшеты андроид 🔥\n")
            file_airpods.write("🎧 AirPods и другие 🎧\n")
            file_watch.write("🔥🔥⌚️ Watch ⌚️🔥🔥\n")
            file_AirTag.write("AirTag 🍏🔘🍏 AirTag\n")
            file_Pencil.write("🖊🖊 Pencil 🖊🖊\n")
            file_Macbook.write("💻 Macbook 💻 🖥Imac 🖥\n")
            file_Dyson.write("🔥 Dyson 🔥\n")
            file_TV.write("📺 Apple TV 📺\n")
            android.write("📱 android 📱\n")
            xbox_ps4.write("🎮 Приставки 🎮\n")
            accessories.write("🪫⌨️🎮 аксессуары 🔥\n")
            column.write("🎼 колонки 🎼\n")
            gopro.write("📷 gopro 📷\n")
            quadrocopter.write("🚁 квадрокоптеры 🚁\n")

            for line in sorted_file:
                if line.lower().__contains__("watch") or line.__contains__("⌚️") or line.__contains__("s8 45 mm") or line.__contains__("s8 45mm") \
                        or line.__contains__("41mm") or line.__contains__("41 mm") or line.__contains__("series 45") \
                        or line.__contains__("40mm") or line.__contains__("45mm") or line.__contains__("44mm") \
                        or line.__contains__("40 mm") or line.__contains__("45 mm") or line.__contains__("44 mm") \
                        or line.__contains__("whatch") or line.__contains__("ultra 49") \
                        or line.__contains__("aw ultra ") or line.__contains__("aw 8/41") \
                        or line.__contains__("aw ultra ") or line.__contains__("aw s7/45") \
                        or line.__contains__("se 44")\
                        or line.__contains__("se 2 40") or line.__contains__("series ultra")\
                        or line.__contains__("s8 45 ") or line.__contains__("s8 41 ") or line.__contains__("se 2 44 ")\
                        or line.__contains__("49mm")or line.__contains__("49 mm") or line.__contains__("aw ultra")or line.__contains__("aw s7/45"):
                    file_watch.write("⌚️" + line)

                elif line.lower().__contains__("airpods") or line.lower().__contains__("air pods")  or line.lower().__contains__("🎧") or \
                        line.lower().__contains__("jbl tune") or line.lower().__contains__("buds") or \
                        line.lower().__contains__("marshall major") or \
                        line.lower().__contains__("sony pulse") :
                    file_airpods.write("🎧" + line)

                elif line.lower().__contains__("realme") or line.lower().__contains__("poco") or line.lower().__contains__("redmi") \
                        or line.lower().__contains__("se3") or line.lower().__contains__("note") \
                        or line.lower().__contains__("honor") or line.lower().__contains__("huawei") \
                        or line.lower().__contains__("pixel") or line.lower().__contains__("oneplus") \
                        or line.lower().__contains__("a03 ") or line.lower().__contains__("a04 ") \
                        or line.lower().__contains__("a04s ") or line.lower().__contains__("a13 ") \
                        or line.lower().__contains__("a32 ") or line.lower().__contains__("a33 ") \
                        or line.lower().__contains__("a52s ") or line.lower().__contains__("a53 ") \
                        or line.lower().__contains__("a73 ") or line.lower().__contains__("a13 ") \
                        or line.lower().__contains__("s21 fe") or line.lower().__contains__("s22 8/128") \
                        or line.lower().__contains__("s22 ultra") or line.lower().__contains__("s22+") \
                        or line.lower().__contains__("s23 ultra") or line.lower().__contains__("a13 ") \
                        or line.lower().__contains__("asus zenfone") or line.lower().__contains__("m1/8/512") \
                        or line.lower().__contains__("m32 6/128") or line.lower().__contains__("m53 8/256") \
                        or line.lower().__contains__("s22 8/256") or line.lower().__contains__("sony xq-ct72") \
                        or line.lower().__contains__("c30s") or line.lower().__contains__("c33 3/32") \
                        or line.lower().__contains__("z flip 4") or line.lower().__contains__("12 lite ") \
                        or line.lower().__contains__("11 lite 5g") or line.lower().__contains__("11t 8/128") \
                        or line.lower().__contains__("11t pro 8/256") or line.lower().__contains__("12x") \
                        or line.lower().__contains__("s21+ 5g") or line.lower().__contains__("12 12/256") \
                        or line.lower().__contains__("12 8/256") or line.lower().__contains__("a52 4/128") \
                        or line.lower().__contains__("a52 8/256") or line.lower().__contains__("p50 pro") \
                        or line.lower().__contains__("sm a047") or line.lower().__contains__("sm a045") \
                        or line.lower().__contains__("sm a042") or line.lower().__contains__("sm a032") \
                        or line.lower().__contains__("sm a325") or line.lower().__contains__("sm a135") \
                        or line.lower().__contains__("a03s 3/32") or line.lower().__contains__("a03s 4/64") \
                        or line.lower().__contains__("s20 fe") or line.lower().__contains__("10c 4/64") \
                        or line.lower().__contains__("s23 8/256") \
                        or line.lower().__contains__("s23+ 8/512") \
                        or line.lower().__contains__("mi ") or line.lower().__contains__("samsung"):
                    android.write("📱" + line)

                elif line.lower().__contains__("macbook") or line.lower().__contains__("mac book") or line.lower().__contains__("imac") \
                        or line.lower().__contains__("mgpm3") or line.lower().__contains__("mgtf3")\
                        or line.lower().__contains__("mjv93") or line.lower().__contains__("mjva3")\
                        or line.lower().__contains__("air m2 512") or line.lower().__contains__("apple studio display")\
                        or line.lower().__contains__("m1 pro/") or line.lower().__contains__("air m2 256/")\
                        or line.lower().__contains__("air m2 256")\
                        or line.lower().__contains__("cpu") or line.lower().__contains__("gpu"):
                    file_Macbook.write("💻" +line)

                elif line.lower().__contains__("usv ") or line.lower().__contains__("usb-c ") \
                        or line.lower().__contains__("mouse ") or line.lower().__contains__("power bank") \
                        or line.lower().__contains__("🔌")  or line.lower().__contains__("sandisk") \
                        or line.lower().__contains__("чехол") \
                        or line.lower().__contains__("20w")  :
                    accessories.write(" " +line)

                elif line.lower().__contains__("iphone") \
                        or line.lower().__contains__("11 512") or line.lower().__contains__("11 64") or line.lower().__contains__("11 128") or line.lower().__contains__("11 256")\
                        or line.lower().__contains__("12 512") or line.lower().__contains__("12 128") or line.lower().__contains__("12 64") or line.lower().__contains__("12 256")\
                        or line.lower().__contains__("13 512") or line.lower().__contains__("13 128") or line.lower().__contains__("13 64") or line.lower().__contains__("13 256")\
                        or line.lower().__contains__("14 512") or line.lower().__contains__("14 128") or line.lower().__contains__("14 1") or line.lower().__contains__("14 256")\
                        or line.lower().__contains__("12 pro 512")or line.lower().__contains__("12 pro 256")or line.lower().__contains__("12 pro 128")or line.lower().__contains__("14 256")\
                        or line.lower().__contains__("14 pro max 512")or line.lower().__contains__("14 pro max 1")or line.lower().__contains__("14 pro max 128")or line.lower().__contains__("14 pro max 256")\
                        or line.lower().__contains__("13 pro max 512")or line.lower().__contains__("13 pro max 1")or line.lower().__contains__("13 pro max 128")or line.lower().__contains__("13 pro max 256")\
                        or line.lower().__contains__("12 pro max 512")or line.lower().__contains__("12 pro max 1")or line.lower().__contains__("12 pro max 128")or line.lower().__contains__("12 pro max 256")\
                        or line.lower().__contains__("11 pro max 512")or line.lower().__contains__("11 pro max 1")or line.lower().__contains__("11 pro max 128")or line.lower().__contains__("11 pro max 256") or line.lower().__contains__("11 pro max 64")\
                        or line.lower().__contains__("11 pro 512")or line.lower().__contains__("11 pro 1")or line.lower().__contains__("11 pro 128")or line.lower().__contains__("11 pro 256")\
                        or line.lower().__contains__("12 pro 512")or line.lower().__contains__("12 pro 1")or line.lower().__contains__("12 pro 128")or line.lower().__contains__("12 pro 256")\
                        or line.lower().__contains__("13 pro 512")or line.lower().__contains__("13 pro 1")or line.lower().__contains__("13 pro 128")or line.lower().__contains__("13 pro 256") \
                        or line.lower().__contains__("14 pro 512") or line.lower().__contains__("14 pro 1") or line.lower().__contains__("14 pro 128") or line.lower().__contains__("14 pro 256") \
                        or line.lower().__contains__("se 128")or line.lower().__contains__("se 2 64 ")or line.lower().__contains__("se 2 128 ")\
                        or line.lower().__contains__("se 64")or line.lower().__contains__("se 3 64 ")or line.lower().__contains__("se 3 128 ")\
                        or line.lower().__contains__("13 mini")\
                        or line.lower().__contains__("12 mini")\
                        or line.lower().__contains__("14 plus")or line.lower().__contains__("xr 128")or line.lower().__contains__("xr 64"):
                    file_iphone.write("📱" + line)

                elif line.lower().__contains__("ipad")  or line.lower().__contains__("keyboard"):
                    file_ipad.write("🍏" + line)

                elif line.lower().__contains__("tablet")  or line.lower().__contains__("tab "):
                    tablet.write("💥" + line)

                elif line.lower().__contains__("pencil") or line.lower().__contains__("🖊"):
                    file_Pencil.write("🖊" + line)

                elif line.lower().__contains__("airtag") or line.lower().__contains__("air tag"):
                    file_AirTag.write("🔘" + line)

                elif line.lower().__contains__("dyson") or line.lower().__contains__("стайлер") \
                        or line.lower().__contains__("hd08") or line.lower().__contains__("airwrap"):
                    file_Dyson.write("👱" +line)

                elif line.lower().__contains__("tv") or line.lower().__contains__("телевизор"):
                    file_TV.write("📺"+line)

                elif line.lower().__contains__("xbox") or line.lower().__contains__("ps4") \
                        or line.lower().__contains__("logitech g29 driving") or line.lower().__contains__("kamera hd для ps")  \
                        or line.lower().__contains__("ps5") or line.lower().__contains__("sony playstation")\
                        or line.lower().__contains__("lunar shift") or line.lower().__contains__("nintendo")  \
                        or line.lower().__contains__("daystrike camo") or line.lower().__contains__("зарядка для джойстика")  :
                    xbox_ps4.write("🎮" +line)

                elif line.lower().__contains__("яндекс") or line.lower().__contains__("колонка") \
                        or line.lower().__contains__("jbl xtreme") or line.lower().__contains__("jbl soundbar") \
                        or line.lower().__contains__("jbl pulse")  or line.lower().__contains__("jbl partybox")  \
                        or line.lower().__contains__("jbl flip") or line.lower().__contains__("jbl boombox")  \
                        or line.lower().__contains__("капсула маруся") \
                        or line.lower().__contains__("jbl charge") \
                        or line.lower().__contains__("jbl 51 channel")  or line.lower().__contains__("homepod")  :
                    column.write("🎼" + line)

                elif line.lower().__contains__('gopro'):
                    gopro.write("📹"+line)

                elif line.lower().__contains__('dji '):
                    quadrocopter.write("🚁" + line)
                else:
                    pass

    except:
        print("Возникла ошибка при сортировке по папкам")


def unique_file():
    with io.open('отсортированный_файл_без_повторений.txt','w', encoding='utf-8', errors='ignore') as output_file, \
            io.open('отсортированный_файл_без_поставщиков/объединение_отсортированных_файлов.txt', "r", encoding='utf-8', errors='ignore') as input_file:
        lines_seen_so_far = set()
        for line in input_file:
            if line not in lines_seen_so_far or line =='\n':
                output_file.write(line)
                lines_seen_so_far.add(line)


def all_to_one_file(file):
    try:
        with io.open(file,'r', encoding='utf-8', errors='ignore') as file_name,\
                io.open('отсортированный_файл_без_поставщиков/объединение_отсортированных_файлов.txt','r',
                        encoding='utf-8', errors='ignore') as file_all_both_r:

            lines = file_all_both_r.readlines()
            lines2 = file_name.readlines()
        with io.open('отсортированный_файл_без_поставщиков/объединение_отсортированных_файлов.txt','r+',
                     encoding='utf-8', errors='ignore') as file_all_both_w:

            file_all_both_w.writelines(lines)
            file_all_both_w.writelines("\n")
            file_all_both_w.writelines(lines2)
    except:
        print("Возникла ошибка при сортировке в одну папку")


def clear_all_to_one_file(file):
    open(file, 'w').close()
    all_to_one_file('отсортированный_файл_без_поставщиков/airpods.txt')
    all_to_one_file('отсортированный_файл_без_поставщиков/AirTag.txt')
    all_to_one_file('отсортированный_файл_без_поставщиков/TV.txt')
    all_to_one_file('отсортированный_файл_без_поставщиков/watch.txt')
    all_to_one_file('отсортированный_файл_без_поставщиков/Айфоны.txt')
    all_to_one_file('отсортированный_файл_без_поставщиков/Dyson.txt')
    all_to_one_file('отсортированный_файл_без_поставщиков/ipad.txt')
    all_to_one_file('отсортированный_файл_без_поставщиков/Планшеты_андроид.txt')
    all_to_one_file('отсортированный_файл_без_поставщиков/Pencil.txt')
    all_to_one_file('отсортированный_файл_без_поставщиков/MacbookImac.txt')
    all_to_one_file('отсортированный_файл_без_поставщиков/android.txt')
    all_to_one_file('отсортированный_файл_без_поставщиков/xbox_ps4.txt')
    all_to_one_file('отсортированный_файл_без_поставщиков/аксессуары.txt')
    all_to_one_file('отсортированный_файл_без_поставщиков/колонки.txt')
    all_to_one_file('отсортированный_файл_без_поставщиков/gopro.txt')
    all_to_one_file('отсортированный_файл_без_поставщиков/квадрокоптеры.txt')


def unic_string(file_big, file_small):
    with open(file_small, 'r', encoding='utf-8') as small, io.open('config_files/conf_file.txt', 'w', encoding='utf-8') as conf_file_w:
        for line in small:
            conf_file_w.write(line[1:])

    with open('config_files/conf_file.txt', 'r', encoding='utf-8') as conf_file_r, \
            open("отсортированный_файл_без_поставщиков/товар_который_не_распределился.txt", 'w', encoding='utf-8') as not_category,\
            open(file_big,'r', encoding='utf-8') as big:
        data = conf_file_r.read()
        for lineb in big:
            if lineb not in data:
                not_category.write(lineb)


def copy_sort_to_without_bad_price():
    with io.open('отсортированный_файл/отсортированный_файл.txt', 'r', encoding='utf-8', errors='ignore') as sort_file_second, io.open(
            'без_лишних_цен/без_лишних_цен.txt', 'w', encoding='utf-8', errors='ignore') as only_need_price_file_write:
        for line_second in sort_file_second.readlines():
            only_need_price_file_write.write(line_second)


def file_without_receiler():
    try:
        with io.open('отсортированный_файл/отсортированный_файл.txt', 'r', encoding='utf-8', errors='ignore') as sorted_file, io.open(
                'отсортированный_файл_без_поставщиков/отсортированный_файл_без_поставщиков.txt', 'w', encoding='utf-8', errors='ignore') as sorted_file_without_receiler:
            for line in sorted_file.readlines():
                my_line = line.split(">>>")
                sorted_file_without_receiler.write(''.join(my_line[:1]) + '\n')

    except:
        print("Возникла ошибка при сортировке")


deleate_old_files()

try:
    check_computer_name()
except:
    print("Ошибка в ПК")
    exit()

try:
    start_to_one_type_of_text_file()
except:
    print("Ошибка в привидении файлов к одному виду")

try:
    cost_upper()
except:
    print("Ошибка в увеличении цен")

try:
    all_in_one_file()
except:
    print("Ошибка в создании единого файла")

try:
    sort()
except:
    print("Ошибка при сортировке")

try:
    file_without_receiler()
except:
    print("Ошибка при создании файла без поставщиков")

try:
    write_to_head("отсортированный_файл/отсортированный_файл.txt")
except:
    print("Ошибка при создании шапки")

try:
    sort_to_files()
except:
    print("Возникла ошибка при сортировке по папкам")


try:
    clear_all_to_one_file('отсортированный_файл_без_поставщиков/объединение_отсортированных_файлов.txt')
except:
    print("объединенный файл не очистился")


try:
    write_to_head("отсортированный_файл_без_поставщиков/отсортированный_файл_без_поставщиков.txt")
    write_to_head("отсортированный_файл_без_поставщиков/объединение_отсортированных_файлов.txt")

except:
    print("Ошибка при создании шапки")

try:
    unic_string( 'отсортированный_файл_без_поставщиков/отсортированный_файл_без_поставщиков.txt','отсортированный_файл_без_поставщиков/объединение_отсортированных_файлов.txt')
except:
    print("Ошибка при распределении товара, который не распределился")

try:
    unique_file()
except:
    print("Ошибка при создании файла с уникальным товаром")
