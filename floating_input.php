<style>

.input-field {
  position: relative;
}

.input-field label {
  position: absolute;
  top: 50%;
  left: 15px;
  transform: translateY(-50%);
  pointer-events: none;
  transition: .3s;

}

input:focus~label,
input:valid~label {
  top: 0;
  padding: 0 10px;
  background: transparent;
  background:#fff;

}

</style>


<!--html-->
<div class="input-field mb-3">
    <input type="text" name="kebele" class="form-control" required spellcheck="false" />
    <label for="">Kebele</label>
</div>
<!---bootsrtap -->
<div class="input-field mb-3">
    <input type="text" name="phone" class="form-control" required spellcheck="false" />
    <label for="">Phone</label>
</div>



