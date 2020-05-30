import jedi

def test_demo():
	code = "abc + 'ss'\na"
	demo = jedi.Script(code, language="demo")

	project = demo._inference_state.project
	project.save()
	path = project._path
	p2 = jedi.api.Project.load(path)
	assert project.language == p2.language

	arr = demo.complete()
	breakpoint()
	# assert arr = ["abc"]
