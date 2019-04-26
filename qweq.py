# @pytest.mark.parametrize('login, password',
#                              [
#                                  ('ruzifawoma@heximail.com', 'Qi3R8Ue4gj8g9BV'),
#                                  ('ruzifawoma@heximail.com', 'QI3R8UE4GJ8G9BV'),
#                                  ('ruzifawoma@heximail.com', 'vfkivjiovppapcv'),
#                                  ('ruzifawoma@heximail.com', '  qi3R8Ue4gj8g9BV')
#                              ])
#
#     def test_unsuccessful_authorization_password(self, login, password):
#         """ Entering valid mail and invalid password to check authorization,
#         getting authorization error message text to verify the text of the error msg"""
#         login_popup = LoginPopup()
#         login_popup.authorize(login, password)
#         assert 'Неправильный адрес электронной почты (email) или пароль' in login_popup.get_error_text_wrong_pass(), \
#             'The text of the error msg about wrong password is different or absent'