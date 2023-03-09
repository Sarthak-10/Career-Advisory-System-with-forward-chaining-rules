from durable.lang import *

course_dict = {
    'dsa': 'Data Structures and Algorithms',
    'ap': 'Advanced Programming',
    'os': 'Operating Systems',
    'dbms': 'Database Management System',
    'ml': 'Machine Learning',
    'ai': 'Artificial Intelligence',
    'dl': 'Deep Learning',
    'ds': 'Data Science',
    'aml': 'Advanced Machine Learning',
    'rl': 'Reinforcement Learning',
    'dw': 'Data Warehousing',
    'dmg': 'Data Mining',
    'nsc': 'Network Security',
    'se': 'Security Engineering',
    'ms': 'Multimedia Security',
    'hci': 'Human Computer Interaction',
    'dpp': 'Design Processes and Perspectives',
    'ctd': 'Circuit Theory and Devices',
    'eld': 'Embedded Logic Design',
    'cn': 'Computer Networks',
    'sns': 'Signals and Systems',
    'ecomm': 'Entrepreneurial Communication',
    'ef': 'Entrepreneurial Finance',
    'ek': 'Entrepreneurial Khichadi',
    'dcs': 'Digital Communication Systems'
}

interest_dict = {
    'puzz': 'Solving Puzzles',
    'how': 'Knowing how things work',
    'comm': 'Communicating with others',
    'sense': 'Making sense out of facts',
    'des': 'Designing stuff',
    'rep': 'Repairing broken toys and appliances'
}

career_dict = {
    'sde': 'Software Development Engineer',
    'mle': 'Machine Learning Engineer',
    'ds': 'Data Scientist',
    'uxd': 'UI/UX Designer',
    'hde': 'Hardware  Engineer',
    'sec': 'Security Engineer',
    'ece': 'Electronics and Communication Engineer',
    'ba': 'Business Analyst'
}

hyper_dict = {
    'sde': 'computer-software-engineer-career',
    'mle': 'computer-information-research-scientist',
    'ds': 'computer-information-research-scientist',
    'uxd': 'usability-specialist-career',
    'hde': 'computer-hardware-engineer-career',
    'sec': 'information-security-analyst',
    'ece': 'electrical-engineer-career',
    'ba': 'financial-analyst-advisor-career'
}

score_gpa = {
    'sde_g': 0.0,
    'mle_g': 0.0,
    'ds_g': 0.0,
    'uxd_g': 0.0,
    'hde_g': 0.0,
    'sec_g': 0.0,
    'ece_g': 0.0,
    'ba_g': 0.0
}

score_interest = {
    'sde_i': 0.0,
    'mle_i': 0.0,
    'ds_i': 0.0,
    'uxd_i': 0.0,
    'hde_i': 0.0,
    'sec_i': 0.0,
    'ece_i': 0.0,
    'ba_i': 0.0
}


def list_items(dic):
    dict_index = dict()
    index = 0
    for i in dic:
        print(index, dic[i])
        dict_index[index] = i
        index += 1
    return dict_index


def input_choice(dict_index):
    lst_index = list(map(int, input().split()))
    lst = [dict_index[i] for i in lst_index]
    return lst


def best_career_option(score_gpa, score_interest):
    c_dic = dict()
    for i in score_gpa:
        c_dic[str(i)[:-2]] = score_gpa[i] + score_interest[str(i)[:-2] + "_i"]
    return max(c_dic, key=c_dic.get)


with ruleset('cgpa_dependence'):
    @when_all(m.dsa >= 0.7)
    def software_enggr(c):
        score = (c.m.ap + c.m.dsa + c.m.os + c.m.dbms) / 4.0
        score_gpa["sde_g"] = score


    @when_all(m.ml >= 0.6)
    def ml_enggr(c):
        score = (c.m.ml + c.m.ai + c.m.dl + c.m.aml + c.m.rl + c.m.ds) / 6.0
        score_gpa["mle_g"] = score


    @when_all(m.ds >= 0.7)
    def data_scientist(c):
        score = (c.m.ds + c.m.dw + c.m.dmg) / 3.0
        score_gpa["ds_g"] = score


    @when_all(m.hci >= 0.8)
    def ux_des(c):
        score = (c.m.hci + c.m.dpp) / 2.0
        score_gpa["uxd_g"] = score


    @when_all(m.ctd >= 0.7)
    def hardware_enggr(c):
        score = (c.m.ctd + c.m.eld) / 2.0
        score_gpa["hde_g"] = score


    @when_all(m.se >= 0.6)
    def sec_enggr(c):
        score = (c.m.nsc + c.m.se + c.m.ms) / 3.0
        score_gpa["sec_g"] = score


    @when_all(m.dcs >= 0.7)
    def ece_enggr(c):
        score = (c.m.dcs + c.m.sns + c.m.cn) / 3.0
        score_gpa["ece_g"] = score


    @when_all(m.ek >= 0.7)
    def bus_analyst(c):
        score = (c.m.ef + c.m.ek + c.m.ecomm) / 3.0
        score_gpa["ba_g"] = score

with ruleset('interest_dependence'):
    @when_all(m.puzz >= 0.7)
    def software_enggr(d):
        score = (d.m.puzz + d.m.how + d.m.sense) / 3.0
        score_interest["sde_i"] = score


    @when_all(m.sense >= 0.8)
    def ml_enggr(d):
        score = (d.m.how + d.m.sense) / 2.0
        score_interest["mle_i"] = score


    @when_all(m.sense >= 0.8)
    def data_scientist(d):
        score = (d.m.how + d.m.sense) / 2.0
        score_interest["ds_i"] = score


    @when_all(m.des >= 0.7)
    def ux_des(d):
        score = (d.m.des + d.m.how) / 2.0
        score_interest["uxd_i"] = score


    @when_all(m.rep >= 0.7)
    def hardware_enggr(d):
        score = (d.m.rep + d.m.des + d.m.puzz) / 3.0
        score_interest["hde_i"] = score


    @when_all(m.how >= 0.7)
    def sec_enggr(d):
        score = (d.m.how + d.m.puzz + d.m.sense) / 3.0
        score_interest["sec_i"] = score


    @when_all(m.rep >= 0.7)
    def ece_enggr(d):
        score = (d.m.rep + d.m.des + d.m.puzz + d.m.how) / 4.0
        score_interest["ece_i"] = score


    @when_all(m.comm >= 0.8)
    def bus_analyst(d):
        score = (d.m.comm + d.m.sense + d.m.how) / 3.0
        score_interest["ba_i"] = score

with ruleset('final_pred'):
    @when_all((m.sde_g >= 0.4) & (m.sde_i >= 0.3))
    def sde(e):
        e.assert_fact({'subject': 'sde'})


    @when_all((m.mle_g >= 0.5) & (m.mle_i >= 0.3))
    def mle(e):
        e.assert_fact({'subject': 'mle'})


    @when_all((m.ds_g >= 0.5) & (m.ds_i >= 0.3))
    def ds(e):
        e.assert_fact({'subject': 'ds'})


    @when_all((m.uxd_g >= 0.4) & (m.uxd_i >= 0.3))
    def uxd(e):
        e.assert_fact({'subject': 'uxd'})


    @when_all((m.hde_g >= 0.6) & (m.hde_i >= 0.4))
    def hde(e):
        e.assert_fact({'subject': 'hde'})


    @when_all((m.sec_g >= 0.6) & (m.sec_i >= 0.4))
    def sec(e):
        e.assert_fact({'subject': 'se'})


    @when_all((m.ba_g >= 0.3) & (m.ba_i >= 0.6))
    def ba(e):
        e.assert_fact({'subject': 'ba'})


    @when_all((m.ece_g >= 0.4) & (m.ece_i >= 0.3))
    def ece(e):
        e.assert_fact({'subject': 'ece'})


    @when_all(+m.subject)
    def output(e):
        print('{0}'.format(career_dict[e.m.subject]))
        print("Career Info :  https://www.careerprofiles.info/{0}.html".format(hyper_dict[e.m.subject]))

if __name__ == '__main__':

    name = input("Enter your name : ")
    print("Hi " + name + ",")
    print("\nWelcome to Career Advisory System\n")
    print('Enter the index of the courses you have taken from the list below:-\n')

    course_dict_index = list_items(course_dict)

    print('\nEnter your choice(space-separated):')
    lst_courses = input_choice(course_dict_index)

    print("\nEnter the grade point scored in the below mentioned subjects:-")

    norm_gpa_lst = []
    for i in lst_courses:
        print("Enter gpa in " + course_dict[i] + " : ", end="")
        norm_gpa_lst.append(float(input()) / 10)

    gpa = dict()
    for i in range(len(lst_courses)):
        gpa[lst_courses[i]] = norm_gpa_lst[i]
    for i in course_dict:
        if i not in gpa:
            gpa[i] = 0.0

    print("\nWhich of the following areas interest you the most:-")

    interest_dict_index = list_items(interest_dict)
    print('\nEnter your choice(space-separated) in order of your preference:')
    lst_interest = input_choice(interest_dict_index)
    interest = dict()
    for i in range(len(lst_interest)):
        interest[lst_interest[i]] = (10.0 - float(i)) / 10.0

    for i in interest_dict:
        if i not in interest:
            interest[i] = 0.0

    assert_fact('cgpa_dependence', gpa)
    assert_fact('interest_dependence', interest)

    combined_dic = dict()
    for i in score_gpa:
        combined_dic[i] = score_gpa[i]
    for i in score_interest:
        combined_dic[i] = score_interest[i]

    try:
        print("\nYour possible carrer options are:-")
        assert_fact('final_pred', combined_dic)
        print("\nThe best career option is:")
        print(career_dict[best_career_option(score_gpa, score_interest)])
    except Exception as e:
        print("\nSorry We could not find any suitable career as per your input")