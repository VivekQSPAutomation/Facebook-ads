# import os
# 
# import allure
# import pytest
# 
# from Config.test_order import Order
# from Influncers_pages.Random_email import Random_Email
# from Influncers_pages.Signup import Signup
# from Influncers_pages.reportCreation import ReportCreation
# 
# 
# class Test_Signup:
#     def signup_object(self, ses_init):
#         self.signup = Signup(ses_init)
#         return self.signup
# 
#     def email_random(self, ses_init):
#         self.random = Random_Email(ses_init)
#         return self.random
# 
#     def refreshdirectory(self):
#         self.refresh = ReportCreation()
#         self.refresh.run_refresh_script(
#             f"{os.getcwd()}/Influncers_pages/DirectoryRefresh.py"
#         )
# 
#     @allure.feature("Signup Functionality")
#     @allure.story("Critical Tests")
#     @allure.severity(allure.severity_level.CRITICAL)
#     @pytest.mark.critical
#     @pytest.mark.run(order=Order.random_email)
#     def test_random_email(self, ses_init, request):
#         self.refreshdirectory()
#         # screen = recording_and_capturing_screen(ses_init, request.node.name)
#         obj = self.email_random(ses_init)
#         status = obj.random_email()
#         if status:
#             print(status)
#             # stop_screen_record(screen)
#             # video_creation_from_screenshots(request.node.name)
#             assert True
#         else:
#             print(status)
#             # stop_screen_record(screen)
#             # video_creation_from_screenshots(request.node.name)
#             assert False
# 
#     @allure.feature("Signup Functionality")
#     @allure.story("Critical Tests")
#     @pytest.mark.critical
#     @pytest.mark.run(order=Order.signup)
#     def test_form_child(self, ses_init, request):
#         # remove_files_in_directory(os.getcwd() + "/screenshots")
#         # screen = recording_and_capturing_screen(ses_init, request.node.name)
#         obj = self.signup_object(ses_init)
#         status = obj.get_form_child()
#         if status:
#             # print(status)
#             # stop_screen_record(screen)
#             # video_creation_from_screenshots(request.node.name)
#             assert True
#         else:
#             # print(status)
#             # stop_screen_record(screen)
#             # video_creation_from_screenshots(request.node.name)
#             assert False
# 
#     @allure.feature("Signup Functionality")
#     @allure.story("Critical Tests")
#     @pytest.mark.run(order=Order.verification_email)
#     def test_verification_email(self, ses_init, request):
#         # remove_files_in_directory(os.getcwd() + "/screenshots")
#         # screen = recording_and_capturing_screen(ses_init, request.node.name)
#         obj = self.email_random(ses_init)
#         status = obj.validation_email()
#         if status:
#             # print(status)
#             # stop_screen_record(screen)
#             # video_creation_from_screenshots(request.node.name)
#             assert True
#         else:
#             # print(status)
#             # stop_screen_record(screen)
#             # video_creation_from_screenshots(request.node.name)
#             assert False
