from datetime import datetime
from dateutil.relativedelta import relativedelta


class calculateCreditScore():
    level_simah = [['300','530','20'],['531','590','40'],['591','670','60'],['671','710','80'],['711','850','100']]
    level_dbr = [['40','50','30'],['25','39','60'],['20','24','80'],['0','19','100']]
    level_age = [['18','23','20'],['24','35','80'],['36','59','100'],['60','75','60']]
    level_income = [['1000','3000','20'],['3001','5000','40'],['5001','9000','60'],['9001','15000','80'],['15000','100']]
    level_marital_status = [['single','100'],['married,divorced','80']]
    level_employer_type = [['student','30'],['freelancer work','40'],['private sector','80'],['government','100']]

    percentage_simah_level = 45/100
    percentage_dbr_level = 18/100
    percentage_age_level = 8/100
    percentage_income_level = 18/100
    percentage_marital_status_level = 6/100
    percentage_employer_type_level = 5/100

    def __init__(self, simah, dbr, age, income, marital_status, employer_type):
        self.simah = int(simah)
        self.dbr = dbr
        # dateformat = "%d-%m-%Y"
        fecha_nacimiento = age
        data_age = relativedelta(datetime.now(), fecha_nacimiento)
        self.age =  data_age.years
        self.income = income
        self.marital_status = marital_status
        self.employer_type = employer_type

    def getPercentage(self):
        percentage_simah = self.getLevel(
            self.level_simah,
            self.percentage_simah_level,
            self.simah
            )
        percentage_dbr = self.getLevel(
            self.level_dbr,
            self.percentage_dbr_level,
            self.dbr
        )
        percentage_age = self.getLevel(
            self.level_age,
            self.percentage_age_level,
            self.age
        )
        percentage_income = self.getLevel(
            self.level_income,
            self.percentage_income_level,
            self.income
        )
        percentage_maritial_status = self.getLevelStr(
            self.level_marital_status,
            self.percentage_marital_status_level,
            self.marital_status
        )
        percentage_employer_type = self.getLevelStr(
            self.level_employer_type,
            self.percentage_employer_type_level,
            self.employer_type
        )
        percentage_total = percentage_simah+percentage_dbr+percentage_age+percentage_income+percentage_maritial_status+percentage_employer_type
        return percentage_total

    def getLevel(self,list, percentage,search):
        for items in list:
            if len(items) == 2:
                if search > int(items[0]):
                    return int(items[1])*percentage
            else:
                if int(items[1]) >= int(search) and int(search) >= int(items[0]):
                    return int(items[2])*percentage

    def getLevelStr(self,list, percentage,search):
        for items in list:
            if items[0] == search:
                return int(items[1])*percentage


if __name__ == "__main__":
    calculate = calculateCreditScore(simah=850, dbr=19, age='12-11-1961', income=850, marital_status='single', employer_type='government')
    calculate.getPercentage()