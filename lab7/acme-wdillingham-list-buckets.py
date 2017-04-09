#wes dillingham
#list all remote buckets

import boto
import boto.s3.connection

conn = boto.connect_s3(
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

for bucket in conn.get_all_buckets():
        print "{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
        )
