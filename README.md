Jive-Community-Management
=========================

Jive Software community management tools using Python and the Jive Rest API.


<h3>Content Management</h3><br />
=========================
<b>ConvertContentToHTML.py</b><br />
Converts content from a space and creates HTML files.<br />

<h3>Group Management</h3><br />
=========================
<b>GetGroupInfo.py</b><br />
Gets a list places and their palceIDs for use in other URIs

<b>GetDeleteGroupInvites.py </b><br/>
Gets a list of invite IDs and deletes them from the group.
  There is no notification to the user of the invited being recinded.
  Update community base URL, username, and password.

<b>GetDeleteGroupMembers.py</b><br/>
Gets a list of all member IDs that are not admins and deletes them from the group.

<b>CreateGroupMember.py</b>
Creates a group membership based upon a personID.
