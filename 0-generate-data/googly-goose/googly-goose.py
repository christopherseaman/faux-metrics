#!/bin/env python3

# This script is used to generate the clickstream data for a fake website.
# Website: goose.birds
# Format: Google Analytics

from faker import Faker
from faker_clickstream import ClickstreamProvider

fake = Faker()
fake.add_provider(ClickstreamProvider)
fake.session_clickstream()
