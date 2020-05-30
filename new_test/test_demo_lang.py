import jedi

def test_demo():
	code = "abc + 'ss'\na"
	demo = jedi.Script(code, language="demo")
	arr = demo.complete()
