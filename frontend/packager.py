from subprocess import call

print 'Building....'

call(['electron-packager','. WSOP --platform=win32 --arch=x64 --version=0.36.0 --overwrite'])
