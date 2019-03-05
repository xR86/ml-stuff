CONFIG = dict({
	'demo_battery': [
		{
			'protocol': 'UDP',
			'setup': 'single',
			'mode': 'simple',
			'size': '1MB',
			'test_count': 1
		}
	],
	'full_battery': [
		{
			'protocol': 'UDP',
			'setup': 'single',
			'mode': 'simple',
			'size': '1MB',
			'test_count': 3
		},
		{
			'protocol': 'UDP',
			'setup': 'single',
			'mode': 'simple',
			'size': '10MB',
			'test_count': 3
		},
		{
			'protocol': 'UDP',
			'setup': 'multi',
			'mode': 'simple',
			'size': '1MB',
			'test_count': 3
		},
		{
			'protocol': 'UDP',
			'setup': 'multi',
			'mode': 'simple',
			'size': '10MB',
			'test_count': 3
		},




		{
			'protocol': 'TCP',
			'setup': 'single',
			'mode': 'simple',
			'size': '1MB',
			'test_count': 3
		},
		{
			'protocol': 'TCP',
			'setup': 'single',
			'mode': 'simple',
			'size': '10MB',
			'test_count': 3
		},
		{
			'protocol': 'TCP',
			'setup': 'multi',
			'mode': 'simple',
			'size': '1MB',
			'test_count': 3
		},
		{
			'protocol': 'TCP',
			'setup': 'multi',
			'mode': 'simple',
			'size': '10MB',
			'test_count': 3
		},

	]
})
