"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import os
from tempfile import NamedTemporaryFile

from django.test import TestCase
from .util import PrivateConfig, PrivateConfigKeyError

class TestPrivateConfig(TestCase):
	def setUp(self):
		f = NamedTemporaryFile(delete=False)
		f.write("""\
[main]
foo = bar
quux = 1
""")
		f.close()
		self.test_cfg = f

	def test_basics(self):
		cfg = PrivateConfig(self.test_cfg.name)
		self.assertTrue("foo" in cfg)
		self.assertTrue("quux" in cfg)
		self.assertTrue("blort" not in cfg)

		self.assertEqual(cfg.foo, "bar")
		self.assertEqual(cfg.quux, "1")

	def test_typemap(self):
		cfg = PrivateConfig(self.test_cfg.name, type_map={"quux": int})
		self.assertTrue("foo" in cfg)
		self.assertTrue("quux" in cfg)
		self.assertEqual(cfg.foo, "bar")
		self.assertEqual(cfg.quux, 1)

	def test_exception(self):
		cfg = PrivateConfig(self.test_cfg.name)
		def get_bad_key():
			return cfg.foobar

		self.assertRaises(PrivateConfigKeyError, get_bad_key)

	def tearDown(self):
		os.unlink(self.test_cfg.name)