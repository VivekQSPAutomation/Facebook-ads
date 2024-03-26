# import datetime
#
# import allure
# import pytest
#
# from Influencers_negative_cases.Negative_compensation import NegativeCompensation_pages
# from Influencers_negative_cases.Negative_creator_Details import NegativeCreatorPages
# from Influencers_negative_cases.Negative_personal_details import NegativePersonal_pages
# from Influencers_negative_cases.negative_general_pages import NegativeCases
#
#
# @pytest.fixture(params=["", "A", "A" * 50, "A" * 300])
# def test_data(request):
#     return request.param
#
#
# @pytest.fixture(
#     params=[
#         datetime.date.today().strftime("%m/%d/%Y"),
#         (datetime.date.today() + datetime.timedelta(days=365 * 1)).strftime("%m/%d/%Y"),
#         (datetime.date.today() + datetime.timedelta(days=-365 * 99)).strftime(
#             "%m/%d/%Y"
#         ),
#         (datetime.date.today() + datetime.timedelta(days=-365 * 18)).strftime(
#             "%m/%d/%Y"
#         ),
#     ]
# )
# def test_date_cases(request):
#     return request.param
#
#
# @pytest.fixture(params=["-1", "0", "1", "2999", "3001", "3000", "5000", "10000", "10" * 10])
# def test_compenstation_data(request):
#     return request.param
#
#
# class TestNegative:
#     @allure.feature("Negative Cases")
#     @allure.story("High Tests")
#     @allure.severity(allure.severity_level.NORMAL)
#     @pytest.mark.high
#     @pytest.mark.run(order=30)
#     def test_negative_general_details(self, test_data, ses_init, request):
#         # remove_files_in_directory(f"{os.getcwd()}/screenshots")
#         # screen = recording_and_capturing_screen(ses_init, request.node.name)
#         obj = NegativeCases(ses_init)
#         obj.general_negative_cases(test_data)
#
#
#     @allure.feature("Negative Cases")
#     @allure.story("High Tests")
#     @allure.severity(allure.severity_level.NORMAL)
#     @pytest.mark.high
#     @pytest.mark.run(order=31)
#     def test_negative_creator_details(self, test_data, ses_init, request):
#         # remove_files_in_directory(f"{os.getcwd()}/screenshots")
#         # screen = recording_and_capturing_screen(ses_init, request.node.name)
#         obj = NegativeCreatorPages(ses_init)
#         obj.get_creator_details(test_data)
#
#
#     @allure.feature("Negative Cases")
#     @allure.story("High Tests")
#     @allure.severity(allure.severity_level.NORMAL)
#     @pytest.mark.high
#     @pytest.mark.run(order=32)
#     def test_negative_compensation(self, test_compenstation_data, ses_init, request):
#         # remove_files_in_directory(f"{os.getcwd()}/screenshots")
#         # screen = recording_and_capturing_screen(ses_init, request.node.name)
#         obj = NegativeCompensation_pages(ses_init)
#         obj.get_compensation_details(test_compenstation_data)
#
#
#     @allure.feature("Negative Cases")
#     @allure.story("High Tests")
#     @allure.severity(allure.severity_level.NORMAL)
#     @pytest.mark.high
#     @pytest.mark.run(order=33)
#     def test_negative_personal_details(self, test_data, ses_init, request):
#         # remove_files_in_directory(f"{os.getcwd()}/screenshots")
#         # screen = recording_and_capturing_screen(ses_init, request.node.name)
#         obj = NegativePersonal_pages(ses_init)
#         obj.get_personal_details(test_data)
#
#
#     @allure.feature("Negative Cases")
#     @allure.story("High Tests")
#     @allure.severity(allure.severity_level.NORMAL)
#     @pytest.mark.high
#     @pytest.mark.run(order=34)
#     def test_negative_personal_date_details(self, test_date_cases, ses_init, request):
#         # remove_files_in_directory(f"{os.getcwd()}/screenshots")
#         # screen = recording_and_capturing_screen(ses_init, request.node.name)
#         obj = NegativePersonal_pages(ses_init)
#         obj.get_personal_date_details(test_date_cases)
#
