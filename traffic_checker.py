import sys


class log_parse:
    
    def parse_log(self, log_name):
        logs = []
        with open(log_name, "r") as full_log_string:
            for lines in full_log_string.readlines():
                line_spliter = lines.split()
                logs.append(line_spliter)
        return logs
    
class log_interface(log_parse):

    def parse_logins(self, lines_from_parse_log):
        all_logins = set()
        for lines in lines_from_parse_log:
            all_logins.add(lines[2])
        return all_logins
    
    def parse_speed(self, logins, lines_from_parse_log):
        sum_download = 0
        sum_upload = 0
        for names in logins: #парсимо логіни
            total_download = 0
            total_upload = 0
            counter = 0
            for lines in lines_from_parse_log: #Парсимо весь лог
                if names in lines[2]: #якщо логін є у лініє тоді робимо наступне
                    counter += 1
                    download = int(lines[5])
                    upload = int(lines[6])
                    total_download += download
                    total_upload += upload
                    sum_download += download
                    sum_upload += upload

            print(f"Логін: {names}"
                  f"\nМегабайт завантажено:\n{total_download / 1000000} MB"
                  f"\nМегабайт вивантажено:\n{total_upload / 1000000} MB"
                  f"\nСумарна кількість запитів від користувача {counter}")
            
        print(f"Усього трафіку спожито в лог файлі: {sys.argv[1]}\n"
              f"Завантажено: {sum_download / 1000000} MB"
              f"\nВивантажено: {sum_upload / 1000000} MB")


logs = log_interface()

#Path of logs
logs_wrapper = logs.parse_log(sys.argv[1])

#return logins
logs_logins = logs.parse_logins(logs_wrapper)


#Traffic Counter
logs.parse_speed(logs_logins, logs_wrapper)
