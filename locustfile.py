
# code to run the file is  -  locust -f locustfile.py 

# from locust import HttpUser, task, between

# TOKEN = "your_access_token_here"
# auth_headers = {"Authorization": f"Bearer {TOKEN}"}

# class AppUser(HttpUser):
#     host = "https://livefan.f2s.live/login"
#     wait_time = between(1, 5)

#     @task
#     def login(self):
#         response = self.client.post("/users/login", json={"email": "fanuser1@yopmail.com", "password": "Fanuser@123"})
#         if response.status_code != 200:
#             self.log_failure("Login failed", response)

#     @task
#     def visit(self):
#         response = self.client.get("/correct/endpoint", headers=auth_headers)
#         if response.status_code != 200:
#             self.log_failure("Request failed", response)

#     def log_failure(self, message, response):
#         self.environment.runner.logger.error(f"{message} - Status Code: {response.status_code}, Response: {response.text}")




# from locust import HttpUser, task,between

# TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI1IiwianRpIjoiYmNjOWZkYjU3ZTI0OGUyN2FjYTk0ZjU2YTE3NDBjMDkxNDI3NGNjM2I3YWUwMDlmZTE0MDBkM2FhYTJjOTI0OTM3YWIxNWY4NWNmNGJiNzIiLCJpYXQiOjE3MDYxODIyNzUuMzExODE5LCJuYmYiOjE3MDYxODIyNzUuMzExODIyLCJleHAiOjE3Mzc4MDQ2NzUuMzA3MjE0LCJzdWIiOiIyMCIsInNjb3BlcyI6W119.OZy_Feg_OFNeug_Z26PzZk4a19JwtjtEgKquacqE6pQtykZRR9vgwDuvlzcxOaLCfwrWva04eJGkYTJW6H-o-Qo7gtmftGY7zFOO0Od1EqwRer8khDXiAgCmY8vF5sZ80YTDz6eyoEuwVSAteyxUEqFs7wRjYZJH0CrW8THotA4boZzz5zPCcc1b3aL8DtP3MWRAv01oRnVDCzRmV9iIZwaSqgP7Z-53KX_f6-zQPFhL_wiHhCO2nYf1RMmN4qu4Ui0jxgCESsu-zBQoQNDWf0-04aX5Tl-XcbTNlFkJp7S6-G7C_uV_m7jFPSACabSX2ph7CFVLB5Xjyv9DNMEYIk5iDzd1tk2qHNJZuyT49VzIfirtH_exDEDz1pK3Is3gfIv2vjzfu2Tp7cqhLRpT0oWn_HhiFVz02O5wKYF5aUidwhtn6kHcVN8CKRruduqL2NtB78rKEp1EFG4WXzbBhxGceTjs-tGZR4xaAabunV6VHM1n-4vsP76cRo9AHmNf02X_OjIKMD4ecu84gtTUc3-gRxUf0GoCYU0uyPL1qLV7l_jU4ZHwm4jDknb-N9-5-obGh2sgQr6fEzzHwA2cxe_j4akj7dJisFVaDGOURd5K8Jh6BLyCqY7G8Dq7pLGDsAzfSmQpFyQpu1q_wGbJHEi70QBLkKx9RIGjhnHw5Lk"
# auth_header = {"Authorization": f"Bearer {TOKEN}"}

# class AppUser(HttpUser):
#     host = "https://livefan.f2s.live/api"
#     wait_time = between(1,5)

#     @task
#     # def visit(self):
#     #     self.client.get("/users/login", headers=auth_header)

#     def on_start(self):
#         self.client.post("/users/login", json={"username":"fanuser1@yopmail.com", "password":"Fanuser@123"})















# from locust import HttpUser, task,between

# TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZjEzM2M4MTdkNzQwMzBmZTQyMWIzMjFkOTBmYzhmYmFkYWUzMzQ4ZmVhMjY5NjVkOWYxOTQyYTk0MzM4NmEzYzk1OGE2MTdhY2EwMTQxOGIiLCJpYXQiOjE2ODQyNDQwODkuNDQ3MDc2LCJuYmYiOjE2ODQyNDQwODkuNDQ3MDc3LCJleHAiOjE3MTU4NjY0ODkuNDQ1NDM1LCJzdWIiOiIyMCIsInNjb3BlcyI6W119.qu5olW_ossxJRnmih5Trw-axIKY2Ikep_imOvr8_JmlHJMn31E2YxEUlxYtfO8hC_zOerGXwYhz7K9ApnJtBS-PP721CrX-EbcnBLUPSCBTWSsLSfaMhdbL2yvLjA7v5Z2rIzvprimdtJpbYkuL6208uwVvviPbHbIYSl1l5Sz_ivD9pD152g4LhMaIOp49I-XmTecjLqEnvr8pBQ2-kMGLcSqmhhCnrluvCX-iFQqY4yED4NiQLKDArnS5Z5-sJWXbTw0xrcPSVx_85il9D0v5XRI6_lzy1vgX-QrIQ_KM8DIESix77CihFuP0Fmm4xdvCip3UxRZS-va3xEB58IJpjaDP9ZBcqm2sKx93rDU8qgojgyhkZW-KFh3jRVaEoHc21WMnWJfpb4Mkv2R8fNovrUbhioYb2YK5zxTjtYQzBnz20x21IMrOFqjk9JWtglSa1XH86x8dC4Nyo5qVmTYShe0OQMoZ7lVKNlIgVI4fOBfkFjOgQw6rVI9YrOvthDgqYtWN9tDo85cLdliCjXs-pn5UAWkKRYDnI5Zguk-oH7zr-HHyNwEcR4ZSFT_DU4FKYsd2NcmrOeddW1L-YBbqVi3ZH3jE1BwtNPi7uMQJZ2pMUWPDvj3E_8TTTCtQArC-aX7fGPPp_tVAGdSXYyy3FHN0mWa3ZUQM8_mGqZNU"
# auth_header = {"Authorization": f"Bearer {TOKEN}"}

# class AppUser(HttpUser):
#     host = "https://crm.colan.in/loginpage/"
#     wait_time = between(1,5)

#     @task
#     def visit(self):
#         self.client.get("/users/login", headers=auth_header)

#     def on_start(self):
#         self.client.post("/users/login", json={"username":"Colanadmincrm", "password":"123789"})

       