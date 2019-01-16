from argparse import RawTextHelpFormatter
from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand

# TODO: Create user groups as well as group-based permissions
class Command(BaseCommand):
	"""
	This command creates user groups on new instances of the sqlite database.
	Run this instead of manually entering groups/permissions in '/admin/' or django's ORM.
	It is useful in development when databases are dropped and created semi-frequently.
	"""
	help = 'Creates User Groups\
			\n-Student\
			\n-Teacher\
			\n-Etc.'

	def handle(self, *args, **options):
		pre_groups = [
		]	

		permissions = [
		]

		groups = []

		self.stdout.write('\nCreating Groups...\n\n')

		for g in pre_groups:
			group = Group.objects.create(name=g)
			groups.append(group)
			self.stdout.write('- %s' % (group.name))

		self.stdout.write(self.style.SUCCESS('\n  Done'))
		self.stdout.write('\nAdding Permissions...')

		# TODO: Decide which groups have what permissions
		for g in groups:
			self.stdout.write('\n%s' % (g.name))
			for p in permissions:
				g.permissions.add(p)
				self.stdout.write('- %s' % (p.name))

		self.stdout.write(self.style.SUCCESS('\n  Done'))

	def create_parser(self, *args, **kwargs):
		parser = super(Command, self).create_parser(*args, **kwargs)
		parser.formatter_class = RawTextHelpFormatter
		return parser
