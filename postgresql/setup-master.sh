#!/bin/bash
cat > "$PGDATA/pg_hba.conf" << EOF
local all all trust
host all all 127.0.0.1/32 trust
local   replication     all                                     trust
host    replication     all             127.0.0.1/32            trust
host    replication     all             ::1/128                 trust
host all all 0.0.0.0/0 scram-sha-256
EOF

cat >> "${PGDATA}/postgresql.conf" << EOF
password_encryption = scram-sha-256
#wal_level = replica
#archive_mode = on
#archive_command = 'cd .'
#max_wal_senders = 8
#wal_keep_segments = 8
#hot_standby = on
EOF
