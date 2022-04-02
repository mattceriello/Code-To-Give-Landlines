
# coding: utf-8

# In[ ]:

import pandas as pd


def book_appointments(schedule, appointments):
    """ Books valid appointments in schedule, and returns new availabletimes in the
    same format as schedule.
    """

    s_df = pd.DataFrame(schedule)
    a_df = pd.DataFrame(appointments)

    pd.options.mode.chained_assignment = None       # to ignore overwriting warning
    for a_index, grp_siz, a_time in a_df.itertuples():
        s_idx_of_time_match = s_df.index[s_df['time'] == a_time].tolist()[0]
        s_df_grp_siz_bfr = s_df[s_idx_of_time_match:s_idx_of_time_match + grp_siz]

        if (s_df_grp_siz_bfr['quota'] > 0).all():   # -1 quotas if rq. times are avail.
            s_df_grp_siz_bfr['quota'] = s_df_grp_siz_bfr['quota'].apply(lambda a: a-1)
    pd.options.mode.chained_assignment = 'warn'     # put it back to default

    new_schedule = list(s_df.to_dict('records'))    # an updated list of available
    return new_schedule                             # times in the same format.

def bookable_times(schedule, grp_siz):
    """ Returns a list of available times for a group size of grp_siz in schedule.
    """

    s_df = pd.DataFrame(schedule)
    bookable_hours = list()

    for s_index, quota, s_time in s_df.loc[s_df['quota'] > 0].itertuples():
        last_idx_with_avail_quota = (s_index + grp_siz)
        if last_idx_with_avail_quota <= s_df.shape[0]:  # don't allow circularity
            if (s_df.iloc[s_index:last_idx_with_avail_quota]['quota'] > 0).all():
                bookable_hours.append(s_time)

    return bookable_hours

def avail_times_for_a_grp_siz(schedule, appointments=None, grp_siz=1):
    """ Returns available times for a group size of grp_siz in schedule given that
    appointments is booked in schedule.
    """

    return bookable_times(book_appointments(schedule, appointments), grp_siz)

if __name__ == "__main__":
    try:
        from FrontendDATA import free_schedule, appointments
    except:
        print("Warning: FrontendDATA.py wasn't found!\n")
        free_schedule = [
            {'quota': 3, 'time': '09:00'},
            {'quota': 3, 'time': '09:20'},
            {'quota': 3, 'time': '09:40'},
            {'quota': 3, 'time': '10:00'},
            {'quota': 3, 'time': '10:20'},
            {'quota': 3, 'time': '10:40'},
            {'quota': 2, 'time': '11:00'},
            {'quota': 2, 'time': '11:20'},
            {'quota': 2, 'time': '11:40'}
        ]
        appointments = [
            {'number_of_people': 2, 'time': '10:40'},
            {'number_of_people': 3, 'time': '09:00'},
            {'number_of_people': 1, 'time': '11:40'},
            {'number_of_people': 2, 'time': '11:20'},
            {'number_of_people': 1, 'time': '09:40'},
            {'number_of_people': 3, 'time': '09:00'},
            {'number_of_people': 4, 'time': '10:00'}
        ]
    input(avail_times_for_a_grp_siz(free_schedule, grp_siz=9))
    df = pd.DataFrame(book_appointments(free_schedule, appointments))
    input(df)
    input(avail_times_for_a_grp_siz(free_schedule))

