import requests

from utilities.resources import ApiResource


def after_scenario(context, scenario):
    if 'library' in scenario.tags:
        deleteBook = context.API + ApiResource.deleteBook
        deleteresp = requests.post(url=deleteBook, json={
            'ID': context.book_id
        }, headers=context.headers)

        assert deleteresp.status_code == 200
        json_delete_resp = deleteresp.json()
        print(json_delete_resp)
        assert json_delete_resp['msg'] == 'book is successfully deleted'


# def before_step(context, step):
#     print('i am before step running because this step is tagged with RUN!!')
