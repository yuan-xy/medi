import jedi

def test_demo():
	code = "first: abc + 'ss'\nsecond: a"
	demo = jedi.Script(code, language="demo")

	project = demo._inference_state.project
	project.save()
	path = project._path
	p2 = jedi.api.Project.load(path)
	assert project.language == p2.language
	
	arr = demo.complete()
	assert len(arr) == 1
	assert arr[0].type == 'keyword'
	assert arr[0].name == 'ademo'

