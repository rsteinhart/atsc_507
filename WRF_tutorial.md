- install things in HOME
- run things in SCRATCH
- to store data for long periods of time use ARCHIVEDIR
/When Running WRF:
- pulls in tools and utils from other places like NETCDF (store gridded earth science data)
- CPPFLAFS looks for headers and find variables defined in which files
- LDFLAGS library files that have subfunctions
  134  make
  135  make check
  136  make install
  137  cd ../
  138  ls
  139  cd include/
  140  ls
  141  cd ..
  142  cd bin/
  143  ls
  144  cd ..
  145  export LIBS=”-lnetcdf”
  146  ls
  147  tar -xvzf netcdf-fortran-4.5.2.tar.gz
  148  cd netcdf-fortran-4.5.2
  149  ls
  150  ./configure --prefix=$NETCDF --disable-shared
  151  export LIBS=-lnetcdf
  152  ./configure --prefix=$NETCDF --disable-shared
  153  make
  154  make check
  155  make install
  156  cd ..
  157  cd bin/
  158  ls
  159  cd ../lib
  160  ls
  161  cd ~
  162  vi ./.bashrc
  163  history

  Thursday:
  - "DC $SCRATCHDIR" for all runs
  - to edit a script press i once in vi
  - to finish editing press esc
  - ":wq" to write and save file
  - "ls -lh geogrid.exe" to see where the link goes to
  - "ln <file name>" to link to a file in another folder
  - ungrib takes national weather service forecast data 