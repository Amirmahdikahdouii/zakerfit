"""
Separate View Files for better handling
in users.py we have all views for regular users.
in coaches.py we have all views for coaches.
"""

from .users import (SignUpView, LoginView, LogOutView, ProfileView, ChangeUserBirthdayView, ChangeUserGenderView,
                    ChangeUserProfileView, RegisterPresentClassView, ChangePresentClassView, VerifyPhoneNumberView,
                    DeletePresentClassView, TimePaymentView, TimePaymentConfirmView)
from .coaches import (CoachProfileView, CoachProfileTimesView, CoachProfileTimesChangeCoachView,
                      CoachProfileTimesChangePlaceCountView,
                      CoachProfileTimesAthletesView, CoachProfileTimesAthletesPresentationView,
                      CoachProfileTimeAthleteProfileView, CoachProfileAddTimeView, CoachProfileClassListView,
                      CoachProfileClassAddCategoryView, CoachProfileClassSelectCategoryView,
                      CoachProfileClassEditCategoryView, CoachProfileClassAddView, CoachProfileClassEditView)
