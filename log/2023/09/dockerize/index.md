# Interactively create dockerfiles

* You have a command in your path, `FROM`.
* You type `FROM some-image:whatever`
* It does something like this:

```bash
echo "FROM $@" > ./Dockerfile
echo >> ./Dockerfile

echo "FROM $@" > $tmpfile
echo "ADD $path/shell /dockerize/shell" >> $tmpfile
tail -n +2 Dockerfile >> $tmpfile || true
echo "ENTRYPOINT /dockerize/shell" >> tmpfile

docker run --build -v$(pwd)/Dockerfile:/dockerize/Dockerfile

Then each command that you type, assuming it succeded, gets added to the Dockerfile.

