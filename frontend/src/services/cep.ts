import { CepResponse } from "@/types/cep";
import axios from "axios";

export async function searchCep(cep: string) {
  const { data } = await axios.get(`https://viacep.com.br/ws/${cep}/json/`);

  if (data.erro) {
    throw new Error("CEP not found");
  }

  return data as CepResponse;
}
