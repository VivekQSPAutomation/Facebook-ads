# import os
#
# import pytest
#
# from Promo_pages.storage import Storage
#
#
# class Test_Git:
#     @pytest.mark.run(order=34)
#     def test_GoogleBucket_push(self):
#         self.google = Storage()
#         source_folder = f"{os.getcwd()}/allure-report"
#         destination_bucket_name = "gs://qspautomation-files/report"
#         self.google.sync_folder(source_folder, destination_bucket_name)
