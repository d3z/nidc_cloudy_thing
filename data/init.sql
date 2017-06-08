CREATE EXTENSION "uuid-ossp";

CREATE TABLE comments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    attendee VARCHAR(100) NOT NULL,
    speaker VARCHAR(100) NOT NULL,
    comment TEXT NOT NULL
);

INSERT INTO comments (attendee, speaker, comment) VALUES ( 'joe@bloggs.com', 'Gareth Fleming', 'God, this was boring');
INSERT INTO comments (attendee, speaker, comment) VALUES ('d@trump.com', 'Gareth Fleming', 'Fake news');