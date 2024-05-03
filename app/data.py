from faker import Faker
import random
import datetime

class DataGenerator:

    def __init__(self):
        self.fake = Faker()

    def generate_formatted_candidate_history(self):
        formatted_history = []
        for _ in range(random.randint(1, 5)):
            history_entry = {
                'job_title': self.fake.job(),
                'lead_status': self.fake.word(),
                'last_updated_at': self.fake.date_time_this_decade().strftime("%Y-%m-%dT%H:%M:%SZ"),  # Convert to RFC3339 format string
                'created_by': self.fake.random_int(min=1, max=100)
            }
            formatted_history.append(history_entry)
        return formatted_history

    def generate_formatted_ctc(self):
        return [{
                'formatted_present_ctc': self.fake.currency_code() + ' ' + str(self.fake.random_number(digits=6)),
                'formatted_expected_ctc': self.fake.currency_code() + ' ' + str(self.fake.random_number(digits=6))
            }]

    def generate_formatted_current_company(self):
        return [
            {
                'from': self.fake.date_this_decade().strftime("%Y-%m-%dT%H:%M:%SZ"),  # Convert to RFC3339 format string
                'profile': self.fake.job(),
                'company': self.fake.company()
            }
        ]

    def generate_formatted_education(self):
        return [
            {
                'passing_year': self.fake.random_int(min=2000, max=2023),
                'college': self.fake.company(),
                'education': self.fake.word()
            }
        ]

    def generate_formatted_previous_company(self):
        return [
            {
                'from': self.fake.date_this_decade().strftime("%Y-%m-%dT%H:%M:%SZ"),  # Convert to RFC3339 format string
                'to': self.fake.date_this_decade().strftime("%Y-%m-%dT%H:%M:%SZ"),    # Convert to RFC3339 format string
                'profile': self.fake.job(),
                'company': self.fake.company()
            }
        ]

    def generate_data(self, num_samples):
        samples = []

        for _ in range(num_samples):
            sample = {
                'accessible_ids': [self.fake.random_int(min=1, max=100) for _ in range(random.randint(1, 5))],
                'age': self.fake.random_int(min=20, max=60),
                'candidate_id': self.fake.random_int(min=1_000_000, max=9_999_999),
                'created_at': self.fake.date_time_this_decade().strftime("%Y-%m-%dT%H:%M:%SZ"),  # Convert to RFC3339 format string
                'creator_name': self.fake.name(),
                'present_ctc': self.fake.random_number(digits=6),
                'current_company': self.fake.company(),
                'current_location': self.fake.address(),
                'education': [self.fake.word() for _ in range(random.randint(1, 5))],
                'expected_ctc': self.fake.random_number(digits=6),
                'experience': float(self.fake.random_number(digits=2)),
                'formatted_candidate_history': self.generate_formatted_candidate_history(),
                'formatted_ctc': self.generate_formatted_ctc(),
                'formatted_current_company': self.generate_formatted_current_company(),
                'formatted_education': self.generate_formatted_education(),
                'formatted_previous_company': self.generate_formatted_previous_company(),
                'gender': self.fake.random_element(elements=('Male', 'Female')),
                'headline': self.fake.sentence(),
                'job_ids': [self.fake.random_int(min=1_000_000, max=9_999_999) for _ in range(random.randint(1, 5))],
                'key_skills': [self.fake.word() for _ in range(random.randint(1, 5))],
                'notice_period': self.fake.random_int(min=1, max=90),
                'organization_id': self.fake.random_int(min=1_000, max=9_999),
                'name': self.fake.name(),
                'other_skills': [self.fake.word() for _ in range(random.randint(1, 5))],
                'preferred_location': [self.fake.city() for _ in range(random.randint(1, 3))],
                'previous_company': [self.fake.company() for _ in range(random.randint(1, 3))],
                'profile': [self.fake.word() for _ in range(random.randint(1, 3))],
                'profile_hash': self.fake.sha256(),
                'resume': self.fake.text(),
                'supplier_ids': [self.fake.random_int(min=1, max=100) for _ in range(random.randint(1, 5))],
                'updated_at': self.fake.date_time_this_decade().strftime("%Y-%m-%dT%H:%M:%SZ")  # Convert to RFC3339 format string
            }
            samples.append(sample)

        return samples
