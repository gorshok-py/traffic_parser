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
        for names in logins: #парсимо логіни
            total_download = 0
            total_upload = 0
            counter = 0
            for lines in lines_from_parse_log: #Парсимо весь лог
                if names in lines[2]: #якщо логін є у лінії тоді робимо наступне
                    counter += 1
                    download = int(lines[5])
                    upload = int(lines[6])
                    total_download += download
                    total_upload += upload



            print(f"Кількість спожитого трафіку для користувача. Логін: {names}\n{total_download / 1000000} Мегабайт завантажено\n{total_upload / 1000000} Мегабайт вивантажено \nСумарна кількість запитів від користувача {counter}")


        
            



logs = log_interface()

#Path of logs
logs_wrapper = logs.parse_log(sys.argv[1])

#return logins
logs_logins = logs.parse_logins(logs_wrapper)


#Traffic Counter
logs.parse_speed(logs_logins, logs_wrapper)
