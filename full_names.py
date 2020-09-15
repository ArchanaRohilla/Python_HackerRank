#!/usr/bin/env python
# coding: utf-8

# In[7]:


def get_full_name(first, last):
    """Return a full name."""
    full_name = "{0} {1}".format(first, last)
    return full_name.title()


# In[8]:


get_full_name("archana", "ahirwar")

