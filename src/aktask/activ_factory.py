"""
O módulo aktask propõe um modelo de acesso a atividades ligadas a issues do github.

"""

import requests
import keyring
from model import Facade


class MainControl:
    def __init__(self):
        self.model = Facade().insert_project("labase")

    def render_data_to_gui(self, writer=None):
        Facade().accept(writer)
        pass

    def fill_with_data(self, reader=None):
        # print(str(os.getenv("AKTASK")))
        s = requests.session()
        s.get('https://activufrj.nce.ufrj.br/', verify=False)
        password = keyring.get_password("activ", "carlo")
        print(password)
        s.post('https://activufrj.nce.ufrj.br/login',
               params=dict(user='carlo', passwd=password, _xsrf=s.cookies['_xsrf']), verify=False)
        issues = s.get('https://activufrj.nce.ufrj.br/rest/activity/labase', verify=False)
        print(issues.text)
        issues = issues.json()['atividades']

        for oid, issue in enumerate(issues):
            Facade().insert_issue("labase", number=oid, title=issue['titulo'], body='',
                                  labels=['@%s' % issue['data_pendent'][:10]],
                                  milestone=issue['grupo'], deadline=issue['deadline'],
                                  assignee=issue['encarregados'],
                                  state=issue['status'], size=0)
ISSUES = {
    'atividades': [
        {'grupo': 'Vitollino', 'data_sort': '2016-11-30 07:32:00.000000',
         'group_id': '7b86125f80044d68b60a938f00273022', 'apagar': True, 'encarregados': ['carlo'],
         'data_pendent': '21/11/2016 16:01', 'deadline': '', 'id': 'd2bf9f0466d44e23921d545cd4bf057a',
         'titulo': 'Tutorial Jardim', 'alterar': True, 'data_start': '30/11/2016 07:32', 'data_end': '',
         'prioritario': 'N', 'status': 'em execucao', 'data_ready': '30/11/2016 07:32'},
        {'grupo': 'Vitollino', 'data_sort': '2016-11-21 16:03:00.000000',
         'group_id': '7b86125f80044d68b60a938f00273022', 'apagar': True, 'encarregados': ['carlo'],
         'data_pendent': '21/11/2016 16:03', 'deadline': '', 'id': '886a4d1665f54b1a97c931b408749e8a',
         'titulo': 'Novel no jardim is-by.us', 'alterar': True, 'data_start': '', 'data_end': '',
         'prioritario': 'N', 'status': 'pendente', 'data_ready': ''},
        {'grupo': 'Kwarwp', 'data_sort': '2016-03-16 11:50:00.000000', 'group_id': '97a8d078de474b8eb68f28364047dfad',
         'apagar': True, 'encarregados': ['carlo'], 'data_pendent': '16/03/2016 11:50', 'deadline': None,
         'id': 'd615759ec68a43828204d311fbd50085', 'titulo': 'Modelos de quest', 'alterar': True,
         'data_start': '16/03/2016 11:50', 'data_end': '', 'prioritario': 'N', 'status': 'pendente', 'data_ready': ''},
        {'grupo': 'Kwarwp', 'data_sort': '2016-04-07 08:12:00.000000', 'group_id': '97a8d078de474b8eb68f28364047dfad',
         'apagar': True, 'encarregados': ['carlo'], 'data_pendent': '07/04/2016 08:12', 'deadline': '',
         'id': '62a9b79d0b7a4eb19ec9374194647ebb', 'titulo': 'Definir padrão de gaming', 'alterar': True,
         'data_start': '07/04/2016 08:12', 'data_end': '', 'prioritario': 'N', 'status': 'em execucao',
         'data_ready': '07/04/2016 08:12'},
        {'grupo': 'Kwarwp', 'data_sort': '2016-11-21 15:36:00.000000', 'group_id': '97a8d078de474b8eb68f28364047dfad',
         'apagar': True, 'encarregados': ['carlo'], 'data_pendent': '21/11/2016 15:36', 'deadline': '',
         'id': 'c3535a0291654a0b868ce38d6dd28b95', 'titulo': 'Aloca personagem', 'alterar': True, 'data_start': '',
         'data_end': '', 'prioritario': 'N', 'status': 'pendente', 'data_ready': ''},
        {'grupo': 'Jardim', 'data_sort': '2016-11-21 16:05:00.000000', 'group_id': '88d43b07027e4f2d8f7cbc25230242ee',
         'apagar': True, 'encarregados': ['carlo'], 'data_pendent': '21/11/2016 16:05', 'deadline': '',
         'id': 'e8a17fcaef4740fcb192a367dcf646d2', 'titulo': 'Elaborar um mapa', 'alterar': True, 'data_start': '',
         'data_end': '', 'prioritario': 'N', 'status': 'pendente', 'data_ready': ''},
        {'grupo': 'Jardim', 'data_sort': '2016-11-21 16:33:00.000000', 'group_id': '88d43b07027e4f2d8f7cbc25230242ee',
         'apagar': True, 'encarregados': ['carlo'], 'data_pendent': '21/11/2016 16:33', 'deadline': '',
         'id': '6c99ce5d488e4a3aa47c70235e78e0c1', 'titulo': 'Cronograma dos Alunos', 'alterar': True, 'data_start': '',
         'data_end': '', 'prioritario': 'N', 'status': 'pendente', 'data_ready': ''},
        {'grupo': 'IGames Antigos', 'data_sort': '2016-11-21 16:36:00.000000',
         'group_id': 'f4a5afee1f6a4f56bdabcaae7e033dbd', 'apagar': True, 'encarregados': ['carlo'],
         'data_pendent': '21/11/2016 16:36', 'deadline': '', 'id': '9e02e301ff2f43adae539b8e65045b8d',
         'titulo': 'Página Activ', 'alterar': True, 'data_start': '', 'data_end': '', 'prioritario': 'N',
         'status': 'pendente', 'data_ready': ''},
        {'grupo': 'IGames Antigos', 'data_sort': '2016-11-21 16:37:00.000000',
         'group_id': 'f4a5afee1f6a4f56bdabcaae7e033dbd', 'apagar': True,
         'encarregados': ['carlo'], 'data_pendent': '21/11/2016 16:37',
         'deadline': '', 'id': '621baac521ad4fe2bdad54960cec1c32',
         'titulo': 'FavIcon Arukas', 'alterar': True, 'data_start': '',
         'data_end': '', 'prioritario': 'N', 'status': 'pendente', 'data_ready': ''},
        {'grupo': 'Graduação', 'data_sort': '', 'group_id': '49354c180d4849cab5dc125d52548448', 'apagar': True,
         'encarregados': '', 'data_pendent': '', 'deadline': '', 'id': '', 'titulo': '', 'alterar': True,
         'data_start': '', 'data_end': '', 'prioritario': '', 'status': '', 'data_ready': ''},
        {'grupo': 'Graduação', 'data_sort': '2016-11-21 16:35:00.000000',
         'group_id': '726569bcd3c146468975b097dc17b39b', 'apagar': True, 'encarregados': ['carlo'],
         'data_pendent': '21/11/2016 16:35', 'deadline': '', 'id': '63713adff7154877bbf1f64bce537497',
         'titulo': 'Página Activ Comp II', 'alterar': True, 'data_start': '', 'data_end': '', 'prioritario': 'N',
         'status': 'pendente', 'data_ready': ''},
        {'grupo': 'Geringato', 'data_sort': '', 'group_id': '856db863e34f406d85f8af160e93933f', 'apagar': True,
         'encarregados': '', 'data_pendent': '', 'deadline': '', 'id': '', 'titulo': '', 'alterar': True,
         'data_start': '', 'data_end': '', 'prioritario': '', 'status': '', 'data_ready': ''}],
    'groupIsFilled': {'49354c180d4849cab5dc125d52548448': True, 'f4a5afee1f6a4f56bdabcaae7e033dbd': True,
                      '97a8d078de474b8eb68f28364047dfad': True, '7b86125f80044d68b60a938f00273022': True,
                      '88d43b07027e4f2d8f7cbc25230242ee': True, '726569bcd3c146468975b097dc17b39b': True}, 'status': 0}
ISSUES = {
    'atividades': [
        {'grupo': 'Vitollino', 'data_sort': '2016-11-30 07:32:00.000000',
         'group_id': '7b86125f80044d68b60a938f00273022', 'apagar': True, 'encarregados': ['carlo'],
         'data_pendent': '21/11/2016 16:01', 'deadline': '', 'id': 'd2bf9f0466d44e23921d545cd4bf057a',
         'titulo': 'Tutorial Jardim', 'alterar': True, 'data_start': '30/11/2016 07:32', 'data_end': '',
         'prioritario': 'N', 'status': 'em execucao', 'data_ready': '30/11/2016 07:32'},
        {'grupo': 'Vitollino', 'data_sort': '2016-11-21 16:03:00.000000',
         'group_id': '7b86125f80044d68b60a938f00273022', 'apagar': True, 'encarregados': ['carlo'],
         'data_pendent': '21/11/2016 16:03', 'deadline': '', 'id': '886a4d1665f54b1a97c931b408749e8a',
         'titulo': 'Novel no jardim is-by.us', 'alterar': True, 'data_start': '', 'data_end': '', 'prioritario': 'N',
         'status': 'pendente', 'data_ready': ''},
        {'grupo': 'Kwarwp', 'data_sort': '2016-03-16 11:50:00.000000', 'group_id': '97a8d078de474b8eb68f28364047dfad',
         'apagar': True, 'encarregados': ['carlo'], 'data_pendent': '16/03/2016 11:50', 'deadline': None,
         'id': 'd615759ec68a43828204d311fbd50085', 'titulo': 'Modelos de quest', 'alterar': True,
         'data_start': '16/03/2016 11:50', 'data_end': '', 'prioritario': 'N', 'status': 'pendente', 'data_ready': ''},
        {'grupo': 'Kwarwp', 'data_sort': '2016-04-07 08:12:00.000000', 'group_id': '97a8d078de474b8eb68f28364047dfad',
         'apagar': True, 'encarregados': ['carlo'], 'data_pendent': '07/04/2016 08:12', 'deadline': '',
         'id': '62a9b79d0b7a4eb19ec9374194647ebb', 'titulo': 'Definir padrão de gaming', 'alterar': True,
         'data_start': '07/04/2016 08:12', 'data_end': '', 'prioritario': 'N', 'status': 'em execucao',
         'data_ready': '07/04/2016 08:12'},
        {'grupo': 'Kwarwp', 'data_sort': '2016-11-21 15:36:00.000000', 'group_id': '97a8d078de474b8eb68f28364047dfad',
         'apagar': True, 'encarregados': ['carlo'], 'data_pendent': '21/11/2016 15:36', 'deadline': '',
         'id': 'c3535a0291654a0b868ce38d6dd28b95', 'titulo': 'Aloca personagem', 'alterar': True, 'data_start': '',
         'data_end': '', 'prioritario': 'N', 'status': 'pendente', 'data_ready': ''},
        {'grupo': 'Jardim', 'data_sort': '2016-11-21 16:05:00.000000', 'group_id': '88d43b07027e4f2d8f7cbc25230242ee',
         'apagar': True, 'encarregados': ['carlo'], 'data_pendent': '21/11/2016 16:05', 'deadline': '',
         'id': 'e8a17fcaef4740fcb192a367dcf646d2', 'titulo': 'Elaborar um mapa', 'alterar': True, 'data_start': '',
         'data_end': '', 'prioritario': 'N', 'status': 'pendente', 'data_ready': ''},
        {'grupo': 'Jardim', 'data_sort': '2016-11-21 16:33:00.000000', 'group_id': '88d43b07027e4f2d8f7cbc25230242ee',
         'apagar': True, 'encarregados': ['carlo'], 'data_pendent': '21/11/2016 16:33', 'deadline': '',
         'id': '6c99ce5d488e4a3aa47c70235e78e0c1', 'titulo': 'Cronograma dos Alunos', 'alterar': True, 'data_start': '',
         'data_end': '', 'prioritario': 'N', 'status': 'pendente', 'data_ready': ''},
        {'grupo': 'IGames Antigos', 'data_sort': '2016-11-21 16:36:00.000000',
         'group_id': 'f4a5afee1f6a4f56bdabcaae7e033dbd', 'apagar': True, 'encarregados': ['carlo'],
         'data_pendent': '21/11/2016 16:36', 'deadline': '15/12/2016 00:00', 'id': '9e02e301ff2f43adae539b8e65045b8d',
         'titulo': 'Página Activ', 'alterar': True, 'data_start': '', 'data_end': '', 'prioritario': 'N',
         'status': 'pendente', 'data_ready': ''}, {'grupo': 'IGames Antigos', 'data_sort': '2016-11-21 16:37:00.000000',
                                                   'group_id': 'f4a5afee1f6a4f56bdabcaae7e033dbd', 'apagar': True,
                                                   'encarregados': ['carlo'], 'data_pendent': '21/11/2016 16:37',
                                                   'deadline': '', 'id': '621baac521ad4fe2bdad54960cec1c32',
                                                   'titulo': 'FavIcon Arukas', 'alterar': True, 'data_start': '',
                                                   'data_end': '', 'prioritario': 'N', 'status': 'pendente',
                                                   'data_ready': ''},
        {'grupo': 'Graduação', 'data_sort': '', 'group_id': '49354c180d4849cab5dc125d52548448', 'apagar': True,
         'encarregados': '', 'data_pendent': '', 'deadline': '', 'id': '', 'titulo': '', 'alterar': True,
         'data_start': '', 'data_end': '', 'prioritario': '', 'status': '', 'data_ready': ''},
        {'grupo': 'Graduação', 'data_sort': '2016-11-21 16:35:00.000000',
         'group_id': '726569bcd3c146468975b097dc17b39b', 'apagar': True, 'encarregados': ['carlo'],
         'data_pendent': '21/11/2016 16:35', 'deadline': '', 'id': '63713adff7154877bbf1f64bce537497',
         'titulo': 'Página Activ Comp II', 'alterar': True, 'data_start': '', 'data_end': '', 'prioritario': 'N',
         'status': 'pendente', 'data_ready': ''},
        {'grupo': 'Geringato', 'data_sort': '', 'group_id': '856db863e34f406d85f8af160e93933f', 'apagar': True,
         'encarregados': '', 'data_pendent': '', 'deadline': '', 'id': '', 'titulo': '', 'alterar': True,
         'data_start': '', 'data_end': '', 'prioritario': '', 'status': '', 'data_ready': ''}],
    'groupIsFilled': {'49354c180d4849cab5dc125d52548448': True, 'f4a5afee1f6a4f56bdabcaae7e033dbd': True,
                      '97a8d078de474b8eb68f28364047dfad': True, '7b86125f80044d68b60a938f00273022': True,
                      '88d43b07027e4f2d8f7cbc25230242ee': True, '726569bcd3c146468975b097dc17b39b': True}, 'status': 0}
