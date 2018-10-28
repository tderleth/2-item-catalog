window.signInCallback = function signInCallback(googleUser) {
  const body = JSON.stringify(googleUser.getAuthResponse().id_token);
  fetch('google-tokensignin', {
    method: 'POST',
    headers: { 'Content-type': 'application/json; charset=UTF-8' },
    body,
  }).then(() => {
    setTimeout(() => {
      window.location.href = '../..';
    }, 500);
  });
};
