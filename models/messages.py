db.election.title.default = 'Election title'

db.election.ballot_model.default = """
<h2>Election Title</h2>

<p>This is a sample ballot!</p>

Ranking Election

<ul>
<li>{{test:ranking}} Candidate A</li>
<li>{{test:ranking}} Candidate B</li>
<li>{{test:ranking}} Candidate C</li>
</ul>

<table>
<tr><td>Candidate 1</td><td>{{0}}</td></tr>
<tr><td>Candidate 2</td><td>{{0}}</td></tr>
<tr><td>Candidate 3</td><td>{{0}}</td></tr>
</table>

<p>or</p>

<table>
<tr><td>Candidate 1</td><td>{{1}} yes</td><td>{{1}} no</td><td>{{1!}} abstain</td></tr>
<tr><td>Candidate 2</td><td>{{2}} yes</td><td>{{2}} no</td><td>{{2!}} abstain</td></tr>
<tr><td>Candidate 3</td><td>{{3}} yes</td><td>{{3}} no</td><td>{{3!}} abstain</td></tr>
</table>
"""

db.election.vote_email.default = """
{{=title}}

Link to vote: {{=link}}
Link to ballots: {{=link_ballots}}
Link to results: {{=link_results}}
"""

db.election.voted_email.default = """
{{=title}}

You have voted and your vote has been registered. Thank you!
Here is your ballot.

Your ballot: {{=link}}
A copy is also attached.

Please keep it to verify the integrity of the election.
"""

db.election.not_voted_email.default = """
{{=title}}

Your ballot: {{=link}}

{{=signature}}
(you did not vote, your BLANK ballot is also attached)
"""

def message_replace(message,**vars):
    message = 'Election N.{{=election_id}} by {{=owner_email}}\n\n' + message
    for key in vars:
        message = message.replace('{{=%s}}' % key, str(vars[key]))
    return message

def meta_send(*args, **kwargs):
    if kwargs.get('sender') == 'i.vote.secure@gmail.com' and GMAIL_LOGIN:
        mail.settings.server = 'smtp.gmail.com:587'
        mail.settings.login = GMAIL_LOGIN
    return mail.send(*args, **kwargs)
