import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const user = {
    status: 'pending',

  };
  const img = {
    status: 'pending',

  };
  try {
    const usersignup = await signUpUser(firstName, lastName);
    user.status = 'fulfilled';
    user.value = usersignup;
  } catch (error) {
    user.status = 'rejected';
    user.value = error.toString();
  }
  try {
    const uploadphoto = await uploadPhoto(fileName);
    img.status = 'fulfilled';
    img.value = uploadphoto;
  } catch (error) {
    img.status = 'rejected';
    img.value = error.toString();
  }
  return [user, img];
}
