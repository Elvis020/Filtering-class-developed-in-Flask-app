class Filter():
    data_list = []
    result = []
    query = {
        "skip": None,
        "take": None
    }

    def __init__(self, data_list, query):
        self.data_list = data_list
        self.query = {**self.query, **query}

    def filter(self):
        # Doing SKip
        skip = self.query['skip']
        if skip is not None:
            self.result = self.data_list[skip:]

        # Doing Take
        take = self.query['take']
        if(take is not None) and (len(self.result) > take):
            self.result = self.result[0:take]

        return self.result


cases = [
    'World',
    'USA',
    'Brazil',
    'India',
    'Russia',
    'South Africa'
]


cases_filter = Filter(cases, {"skip": 1, "take": 6})
filtered = cases_filter.filter()

print(len(filtered))
print(filtered)
